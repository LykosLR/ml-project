#python -m streamlit run app.py


import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st
from scipy import stats

# ─────────────────────────────────────────────
#  Configuración de página
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="EDA Interactivo",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

ACCENT   = "#4F8FF7"
SUCCESS  = "#27AE60"
WARNING  = "#E67E22"
DANGER   = "#E74C3C"
PALETTE  = px.colors.qualitative.Set2

# ─────────────────────────────────────────────
#  Helpers de carga
# ─────────────────────────────────────────────
@st.cache_data
def load_clasificacion(path: str = "dataset_clasificacion.csv") -> pd.DataFrame:
    df = pd.read_csv(path)
    df.columns = df.columns.str.strip()
    str_cols = df.select_dtypes(include="object").columns
    for c in str_cols:
        df[c] = df[c].str.strip().str.lower()
    # eliminar columnas constantes
    constant = [c for c in df.columns if df[c].nunique() <= 1]
    df = df.drop(columns=constant)
    return df


@st.cache_data
def load_regresion(path: str = "dataset_regresion.csv") -> pd.DataFrame:
    df = pd.read_csv(path)
    df = df.drop(columns=[c for c in df.columns if c.startswith("Unnamed")], errors="ignore")
    df.columns = df.columns.str.strip()
    # Limpiar CGPA outliers evidentes (>5 es imposible en escala 4.0 o 10.0 típica)
    target = "What is your current CGPA?"
    df[target] = pd.to_numeric(df[target], errors="coerce")
    df = df[df[target].between(0, 5)].copy()
    return df


# ─────────────────────────────────────────────
#  Función de métricas
# ─────────────────────────────────────────────
def metric_card(label: str, value, delta=None, color=ACCENT):
    delta_html = f"<span style='font-size:0.85rem;color:#888'>{delta}</span>" if delta else ""
    st.markdown(
        f"""
        <div style='background:#1E2130;border-radius:10px;padding:18px 22px;border-left:4px solid {color};'>
            <p style='margin:0;font-size:0.8rem;color:#AAA;letter-spacing:0.05em'>{label}</p>
            <p style='margin:4px 0 0;font-size:1.8rem;font-weight:700;color:#FFF'>{value}</p>
            {delta_html}
        </div>
        """,
        unsafe_allow_html=True,
    )


# ═════════════════════════════════════════════
#  PESTAÑA 1 — CLASIFICACIÓN
# ═════════════════════════════════════════════
def tab_clasificacion():
    st.header("🏢 IBM HR Analytics — Rotación de Empleados (Attrition)")
    st.markdown("Dataset con **1 470 empleados** y **35 variables** originales. "
                "La variable objetivo es **Attrition** (¿abandonó la empresa?).")

    try:
        df = load_clasificacion()
    except FileNotFoundError:
        st.error("No se encontró `dataset_clasificacion.csv` en la carpeta actual.")
        return

    TARGET = "Attrition"
    num_cols = df.select_dtypes(include="number").columns.tolist()
    cat_cols = [c for c in df.select_dtypes(include="object").columns if c != TARGET]

    # ── Sidebar ──────────────────────────────
    with st.sidebar:
        st.subheader("⚙️ Filtros — Clasificación")
        dept_opts = ["Todos"] + sorted(df["Department"].unique().tolist())
        dept_sel  = st.selectbox("Departamento", dept_opts)
        gender_opts = ["Todos"] + sorted(df["Gender"].unique().tolist())
        gender_sel  = st.selectbox("Género", gender_opts)
        age_range   = st.slider("Rango de Edad", int(df["Age"].min()), int(df["Age"].max()),
                                (int(df["Age"].min()), int(df["Age"].max())))

    mask = (df["Age"].between(*age_range))
    if dept_sel   != "Todos": mask &= df["Department"] == dept_sel
    if gender_sel != "Todos": mask &= df["Gender"]     == gender_sel
    dff = df[mask].copy()

    # ── KPIs ─────────────────────────────────
    yes_rate = (dff[TARGET] == "yes").mean() * 100
    n_yes    = (dff[TARGET] == "yes").sum()
    n_no     = (dff[TARGET] == "no").sum()
    avg_inc  = dff["MonthlyIncome"].mean()

    k1, k2, k3, k4 = st.columns(4)
    with k1: metric_card("Total Empleados",   f"{len(dff):,}")
    with k2: metric_card("Rotaron (Yes)",     f"{n_yes:,}",  f"{yes_rate:.1f}%", DANGER)
    with k3: metric_card("Se quedaron (No)",  f"{n_no:,}",   f"{100-yes_rate:.1f}%", SUCCESS)
    with k4: metric_card("Ingreso Mensual Prom.", f"${avg_inc:,.0f}")

    st.markdown("---")

    # ── Distribución del Target ───────────────
    c1, c2 = st.columns([1, 2])
    with c1:
        st.subheader("Distribución de Attrition")
        counts = dff[TARGET].value_counts().reset_index()
        counts.columns = ["Attrition", "Count"]
        fig = px.pie(counts, names="Attrition", values="Count",
                     color_discrete_sequence=[SUCCESS, DANGER],
                     hole=0.45)
        fig.update_traces(textinfo="percent+label")
        fig.update_layout(showlegend=False, margin=dict(t=10, b=10, l=10, r=10),
                          paper_bgcolor="rgba(0,0,0,0)", font_color="#EEE")
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        st.subheader("Attrition por Departamento y Género")
        gdf = (dff.groupby(["Department", "Gender", TARGET])
                  .size().reset_index(name="n"))
        gdf["pct"] = gdf.groupby(["Department", "Gender"])["n"].transform(lambda x: x/x.sum()*100)
        gdf_yes = gdf[gdf[TARGET] == "yes"]
        fig2 = px.bar(gdf_yes, x="Department", y="pct", color="Gender",
                      barmode="group", text_auto=".1f",
                      labels={"pct": "% Attrition", "Department": "Departamento"},
                      color_discrete_sequence=PALETTE)
        fig2.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                           font_color="#EEE", legend_title_text="Género")
        st.plotly_chart(fig2, use_container_width=True)

    st.markdown("---")

    # ── Análisis Univariado ───────────────────
    st.subheader("🔍 Análisis Univariado por Variable Numérica")
    col_sel = st.selectbox("Selecciona variable numérica", num_cols, index=num_cols.index("MonthlyIncome"))

    c3, c4 = st.columns(2)
    with c3:
        fig3 = px.histogram(dff, x=col_sel, color=TARGET,
                            barmode="overlay", nbins=30, opacity=0.75,
                            color_discrete_map={"yes": DANGER, "no": SUCCESS},
                            labels={TARGET: "Attrition"})
        fig3.update_layout(title=f"Distribución de {col_sel}",
                           paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                           font_color="#EEE")
        st.plotly_chart(fig3, use_container_width=True)

    with c4:
        fig4 = px.box(dff, x=TARGET, y=col_sel, color=TARGET,
                      color_discrete_map={"yes": DANGER, "no": SUCCESS},
                      points="outliers",
                      labels={TARGET: "Attrition", col_sel: col_sel})
        fig4.update_layout(title=f"Box Plot: {col_sel} vs Attrition",
                           showlegend=False,
                           paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                           font_color="#EEE")
        st.plotly_chart(fig4, use_container_width=True)

    st.markdown("---")

    # ── Variable Categórica ───────────────────
    st.subheader("📊 Attrition por Variable Categórica")
    cat_sel = st.selectbox("Selecciona variable categórica", cat_cols,
                           index=cat_cols.index("JobRole") if "JobRole" in cat_cols else 0)

    gdf2 = (dff.groupby([cat_sel, TARGET]).size().reset_index(name="n"))
    gdf2["pct"] = gdf2.groupby(cat_sel)["n"].transform(lambda x: x/x.sum()*100)

    fig5 = px.bar(gdf2, x=cat_sel, y="pct", color=TARGET, barmode="stack",
                  text_auto=".1f",
                  color_discrete_map={"yes": DANGER, "no": SUCCESS},
                  labels={"pct": "% del grupo", cat_sel: cat_sel, TARGET: "Attrition"})
    fig5.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                       font_color="#EEE", xaxis_tickangle=-35)
    st.plotly_chart(fig5, use_container_width=True)

    st.markdown("---")

    # ── Correlación ───────────────────────────
    st.subheader("🔗 Mapa de Correlación")
    corr = dff[num_cols].corr()
    fig6 = px.imshow(corr, text_auto=".2f", aspect="auto",
                     color_continuous_scale="RdBu_r", zmin=-1, zmax=1)
    fig6.update_layout(paper_bgcolor="rgba(0,0,0,0)", font_color="#EEE",
                       height=500, title="Correlación entre variables numéricas")
    st.plotly_chart(fig6, use_container_width=True)

    st.markdown("---")

    # ── Scatter Interactivo ───────────────────
    st.subheader("🔵 Scatter Plot Interactivo")
    sc1, sc2, sc3 = st.columns(3)
    x_ax = sc1.selectbox("Eje X", num_cols, index=num_cols.index("MonthlyIncome"))
    y_ax = sc2.selectbox("Eje Y", num_cols, index=num_cols.index("YearsAtCompany"))
    sz_ax = sc3.selectbox("Tamaño (opcional)", ["Ninguno"] + num_cols)

    fig7 = px.scatter(dff, x=x_ax, y=y_ax,
                      color=TARGET,
                      size=sz_ax if sz_ax != "Ninguno" else None,
                      color_discrete_map={"yes": DANGER, "no": SUCCESS},
                      opacity=0.65, hover_data=["JobRole", "Department"],
                      labels={TARGET: "Attrition"})
    fig7.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                       font_color="#EEE")
    st.plotly_chart(fig7, use_container_width=True)

    st.markdown("---")

    # ── Tabla de datos ────────────────────────
    with st.expander("📋 Ver datos filtrados"):
        st.dataframe(dff.head(200), use_container_width=True)
        st.caption(f"Mostrando hasta 200 de {len(dff)} filas filtradas.")


# ═════════════════════════════════════════════
#  PESTAÑA 2 — REGRESIÓN
# ═════════════════════════════════════════════
def tab_regresion():
    st.header("🎓 Predicción de CGPA Estudiantil — Regresión")
    st.markdown("Dataset con **894 estudiantes universitarios** y múltiples variables académicas "
                "y socioeconómicas. La variable objetivo es el **CGPA actual**.")

    try:
        df = load_regresion()
    except FileNotFoundError:
        st.error("No se encontró `dataset_regresion.csv` en la carpeta actual.")
        return

    TARGET = "What is your current CGPA?"

    # Nombres cortos para UI
    SHORT = {
        "What is your current CGPA?":                                "CGPA actual",
        "What was your previous SGPA?":                              "SGPA previo",
        "How many hour do you study daily? (Hours )":                "Horas estudio/día",
        "How many times do you seat for study in a day?":            "Sesiones estudio/día",
        "How many hour do you spent daily in social media? (Hours)": "Horas redes sociales/día",
        "How many hour do you spent daily on your skill development? (Hours )": "Horas desarrollo skills/día",
        "Average attendance on class (Percentage )":                 "Asistencia (%)",
        "Current Semester":                                          "Semestre actual",
        "Age (Years)":                                               "Edad",
        "How many Credit did you have completed?":                   "Créditos completados",
        "What is your monthly Family Income ":                       "Ingreso familiar mensual",
    }

    num_cols_raw = [TARGET, "What was your previous SGPA?",
                    "How many hour do you study daily? (Hours )",
                    "How many times do you seat for study in a day?",
                    "How many hour do you spent daily in social media? (Hours)",
                    "How many hour do you spent daily on your skill development? (Hours )",
                    "Average attendance on class (Percentage )",
                    "Current Semester", "Age (Years)",
                    "How many Credit did you have completed?",
                    "What is your monthly Family Income "]
    num_cols_raw = [c for c in num_cols_raw if c in df.columns]

    cat_cols_raw = ["Gender", "Program",
                    "Do you have meritorious scholarship ?",
                    "What is your preferable learning mode?",
                    "Status of your English language proficiency",
                    "Did you ever fall in probation?",
                    "Are you engaged with any co-curriculum activities?",
                    "Do you have personal Computer?"]
    cat_cols_raw = [c for c in cat_cols_raw if c in df.columns]

    dff = df.dropna(subset=[TARGET]).copy()

    # ── Sidebar ──────────────────────────────
    with st.sidebar:
        st.subheader("⚙️ Filtros — Regresión")
        if "Program" in dff.columns:
            prog_opts = ["Todos"] + sorted(dff["Program"].dropna().unique().tolist())
            prog_sel  = st.selectbox("Programa", prog_opts)
        else:
            prog_sel = "Todos"
        if "Gender" in dff.columns:
            gen_opts  = ["Todos"] + sorted(dff["Gender"].dropna().unique().tolist())
            gen_sel   = st.selectbox("Género", gen_opts)
        else:
            gen_sel = "Todos"
        cgpa_range = st.slider("Rango CGPA", 0.0, 5.0, (0.0, 5.0), step=0.1)

    mask = dff[TARGET].between(*cgpa_range)
    if prog_sel != "Todos" and "Program" in dff.columns:
        mask &= dff["Program"] == prog_sel
    if gen_sel != "Todos" and "Gender" in dff.columns:
        mask &= dff["Gender"] == gen_sel
    dff = dff[mask].copy()

    # ── KPIs ─────────────────────────────────
    k1, k2, k3, k4 = st.columns(4)
    with k1: metric_card("Estudiantes",    f"{len(dff):,}")
    with k2: metric_card("CGPA Promedio",  f"{dff[TARGET].mean():.3f}", color=ACCENT)
    with k3: metric_card("CGPA Mediana",   f"{dff[TARGET].median():.3f}", color=SUCCESS)
    with k4: metric_card("Desv. Estándar", f"{dff[TARGET].std():.3f}", color=WARNING)

    st.markdown("---")

    # ── Distribución del Target ───────────────
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("Distribución del CGPA")
        fig = px.histogram(dff, x=TARGET, nbins=30, color_discrete_sequence=[ACCENT],
                           labels={TARGET: "CGPA actual"})
        fig.add_vline(x=dff[TARGET].mean(), line_dash="dash", line_color=WARNING,
                      annotation_text=f"Media: {dff[TARGET].mean():.2f}")
        fig.add_vline(x=dff[TARGET].median(), line_dash="dot", line_color=SUCCESS,
                      annotation_text=f"Mediana: {dff[TARGET].median():.2f}")
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                          font_color="#EEE")
        st.plotly_chart(fig, use_container_width=True)

    with c2:
        if "Program" in dff.columns:
            st.subheader("CGPA por Programa")
            fig2 = px.box(dff, x="Program", y=TARGET, color="Program",
                          color_discrete_sequence=PALETTE,
                          labels={TARGET: "CGPA", "Program": "Programa"})
            fig2.update_layout(showlegend=False, xaxis_tickangle=-35,
                               paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                               font_color="#EEE")
            st.plotly_chart(fig2, use_container_width=True)

    st.markdown("---")

    # ── Correlación con CGPA ─────────────────
    st.subheader("📈 Correlación de Variables Numéricas con CGPA")
    num_df = dff[num_cols_raw].dropna()
    corr_target = (num_df.corr()[TARGET]
                         .drop(TARGET)
                         .sort_values(key=abs, ascending=False))

    colors = [DANGER if v < 0 else SUCCESS for v in corr_target]
    fig3 = go.Figure(go.Bar(
        x=corr_target.values,
        y=[SHORT.get(c, c) for c in corr_target.index],
        orientation="h",
        marker_color=colors,
        text=[f"{v:.3f}" for v in corr_target.values],
        textposition="outside",
    ))
    fig3.update_layout(xaxis_title="Correlación de Pearson", yaxis_title="",
                       paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                       font_color="#EEE", height=400,
                       xaxis=dict(range=[-1, 1]))
    st.plotly_chart(fig3, use_container_width=True)

    st.markdown("---")

    # ── Scatter vs Variable Numérica ─────────
    st.subheader("🔵 Relación con CGPA")
    num_choices = [c for c in num_cols_raw if c != TARGET]
    x_sel = st.selectbox("Variable X", num_choices,
                         format_func=lambda c: SHORT.get(c, c),
                         index=0)

    color_by = None
    if "Program" in dff.columns:
        color_by = "Program"

    fig4 = px.scatter(dff, x=x_sel, y=TARGET, color=color_by,
                      trendline="ols", opacity=0.65,
                      color_discrete_sequence=PALETTE,
                      labels={TARGET: "CGPA actual", x_sel: SHORT.get(x_sel, x_sel)})
    fig4.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                       font_color="#EEE")
    st.plotly_chart(fig4, use_container_width=True)

    # Estadística de regresión simple
    sub = dff[[x_sel, TARGET]].dropna()
    if len(sub) > 5:
        slope, intercept, r, p, _ = stats.linregress(sub[x_sel], sub[TARGET])
        st.info(f"**Regresión lineal simple** — R² = {r**2:.4f} | "
                f"pendiente = {slope:.4f} | p-valor = {p:.4e}")

    st.markdown("---")

    # ── CGPA por Variable Categórica ─────────
    st.subheader("📊 CGPA por Variable Categórica")
    CAT_LABELS = {c: c.replace("Do you ", "").replace("?", "").replace("What is ", "").strip().capitalize()
                  for c in cat_cols_raw}
    cat_sel = st.selectbox("Variable categórica", cat_cols_raw,
                           format_func=lambda c: CAT_LABELS.get(c, c))

    dff_cat = dff[[cat_sel, TARGET]].dropna()
    fig5 = px.box(dff_cat, x=cat_sel, y=TARGET, color=cat_sel,
                  color_discrete_sequence=PALETTE, points="outliers",
                  labels={TARGET: "CGPA actual", cat_sel: CAT_LABELS.get(cat_sel, cat_sel)})
    fig5.update_layout(showlegend=False, xaxis_tickangle=-30,
                       paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                       font_color="#EEE")
    st.plotly_chart(fig5, use_container_width=True)

    # Test ANOVA
    groups = [g[TARGET].dropna().values for _, g in dff_cat.groupby(cat_sel) if len(g) > 1]
    if len(groups) >= 2:
        f_stat, p_val = stats.f_oneway(*groups)
        color = "🟢" if p_val < 0.05 else "🔴"
        st.info(f"{color} **ANOVA** — F = {f_stat:.3f} | p-valor = {p_val:.4e} | "
                f"{'Diferencia significativa (α=0.05)' if p_val < 0.05 else 'Sin diferencia significativa'}")

    st.markdown("---")

    # ── Matriz de Correlación ─────────────────
    st.subheader("🔗 Mapa de Correlación entre Variables Numéricas")
    corr_full = num_df.rename(columns=SHORT).corr()
    fig6 = px.imshow(corr_full, text_auto=".2f", aspect="auto",
                     color_continuous_scale="RdBu_r", zmin=-1, zmax=1)
    fig6.update_layout(paper_bgcolor="rgba(0,0,0,0)", font_color="#EEE", height=500)
    st.plotly_chart(fig6, use_container_width=True)

    st.markdown("---")

    # ── Tabla ─────────────────────────────────
    with st.expander("📋 Ver datos filtrados"):
        st.dataframe(dff.head(200), use_container_width=True)
        st.caption(f"Mostrando hasta 200 de {len(dff)} filas filtradas.")


# ═════════════════════════════════════════════
#  MAIN
# ═════════════════════════════════════════════
def main():
    st.markdown("""
        <style>
            .block-container { padding-top: 1.5rem; }
            [data-testid="stSidebar"] { background: #111827; }
            h1, h2, h3 { color: #F0F4FF; }
        </style>
    """, unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["🏢 Clasificación — Attrition", "🎓 Regresión — CGPA"])
    with tab1:
        tab_clasificacion()
    with tab2:
        tab_regresion()


if __name__ == "__main__":
    main()