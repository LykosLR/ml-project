import os
import sqlite3
from pathlib import Path
import pandas as pd

# ---------------------------------Crear base de datos y cargar CSVs---------------------------------
DB_PATH = Path(__file__).parent.parent / "data" / "processed" / "database.db"
CSV_PATH = Path(__file__).parent.parent / "data" / "raw"
os.makedirs(DB_PATH.parent, exist_ok=True)



conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

print("=" * 60)
print("  BASE DE DATOS CREADA EN:", DB_PATH)
print("=" * 60)

# --------------------------------Crear la tablas ---------------------------------------

# --- Tabla Clasificacion ---
df_clas = pd.read_csv(CSV_PATH / "dataset_clasificacion.csv")
df_clas.to_sql("Clasificacion", conn, if_exists="replace", index=False)
print(f"\n Tabla 'Clasificacion' creada con {len(df_clas)} registros y {len(df_clas.columns)} columnas.")

# --- Tabla Regresion ---
df_reg = pd.read_csv(CSV_PATH / "dataset_regresion.csv")
df_reg.to_sql("Regresion", conn, if_exists="replace", index=False)
print(f" Tabla 'Regresion' creada con {len(df_reg)} registros y {len(df_reg.columns)} columnas.")

# ------------------------------ Función para ejecutar consultas --------------------------------

def ejecutar(pregunta, sql, columnas):
    print("\n" + "─" * 60)
    print(f" {pregunta}")
    print("─" * 60)
    df = pd.read_sql_query(sql, conn)
    df.columns = columnas
    print(df.to_string(index=False))



print("\n\n" + "═" * 60)
print("  CONSULTAS SOBRE LA TABLA: Clasificacion")
print("═" * 60)

# ── Q1: Cantidad de Yes en Attrition ──────────
ejecutar(
    "Q1 · ¿Cuántos empleados tienen Attrition = 'Yes'?",
    """
    SELECT COUNT(*) AS total_yes
    FROM Clasificacion
    WHERE Attrition = 'Yes'
    """,
    ["Total Attrition Yes"]
)

# ── Q2: Cantidad de No en Attrition ───────────
ejecutar(
    "Q2 · ¿Cuántos empleados tienen Attrition = 'No'?",
    """
    SELECT COUNT(*) AS total_no
    FROM Clasificacion
    WHERE Attrition = 'No'
    """,
    ["Total Attrition No"]
)

# ── Q3: Promedio y mediana de DailyRate ───────
ejecutar(
    "Q3 · ¿Cuál es el promedio y la mediana de DailyRate?",
    """
    SELECT
        ROUND(AVG(DailyRate), 2)    AS promedio_daily_rate,
        (
            SELECT DailyRate
            FROM Clasificacion
            ORDER BY DailyRate
            LIMIT 1
            OFFSET (SELECT COUNT(*) FROM Clasificacion) / 2
        )                           AS mediana_daily_rate
    FROM Clasificacion
    """,
    ["Promedio DailyRate", "Mediana DailyRate"]
)

# ── Q4: Mínimo y máximo de DistanceFromHome ───
ejecutar(
    "Q4 · ¿Cuál es el valor mínimo y máximo de DistanceFromHome?",
    """
    SELECT
        MIN(DistanceFromHome) AS minimo_distancia,
        MAX(DistanceFromHome) AS maximo_distancia
    FROM Clasificacion
    """,
    ["Mínimo DistanceFromHome", "Máximo DistanceFromHome"]
)

# ── Q5: Conteo por nivel educativo ────────────
ejecutar(
    "Q5 · ¿Cuántas personas hay por cada nivel educativo?",
    """
    SELECT
        CASE Education
            WHEN 1 THEN '1 - Below College'
            WHEN 2 THEN '2 - College'
            WHEN 3 THEN '3 - Bachelor'
            WHEN 4 THEN '4 - Master'
            WHEN 5 THEN '5 - Doctor'
        END  AS nivel_educativo,
        COUNT(*) AS total
    FROM Clasificacion
    GROUP BY Education
    ORDER BY Education
    """,
    ["Nivel Educativo", "Total"]
)

# ── Q6: Attrition Yes/No por nivel educativo ─
ejecutar(
    "Q6 · ¿Cuántos tienen Attrition Yes y No por nivel educativo?",
    """
    SELECT
        CASE Education
            WHEN 1 THEN '1 - Below College'
            WHEN 2 THEN '2 - College'
            WHEN 3 THEN '3 - Bachelor'
            WHEN 4 THEN '4 - Master'
            WHEN 5 THEN '5 - Doctor'
        END                                      AS nivel_educativo,
        SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END) AS attrition_yes,
        SUM(CASE WHEN Attrition='No'  THEN 1 ELSE 0 END) AS attrition_no
    FROM Clasificacion
    GROUP BY Education
    ORDER BY Education
    """,
    ["Nivel Educativo", "Attrition Yes", "Attrition No"]
)

# ── Q7: Conteo y Attrition por EnvironmentSatisfaction ──
ejecutar(
    "Q7 · ¿Cuántas personas hay por nivel de EnvironmentSatisfaction y cuántos tienen Attrition Yes/No?",
    """
    SELECT
        CASE EnvironmentSatisfaction
            WHEN 1 THEN '1 - Low'
            WHEN 2 THEN '2 - Medium'
            WHEN 3 THEN '3 - High'
            WHEN 4 THEN '4 - Very High'
        END                                      AS satisfaccion_ambiente,
        COUNT(*)                                 AS total,
        SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END) AS attrition_yes,
        SUM(CASE WHEN Attrition='No'  THEN 1 ELSE 0 END) AS attrition_no
    FROM Clasificacion
    GROUP BY EnvironmentSatisfaction
    ORDER BY EnvironmentSatisfaction
    """,
    ["Satisfacción Ambiente", "Total", "Attrition Yes", "Attrition No"]
)

# ── Q8: Conteo por género y Attrition ─────────
ejecutar(
    "Q8 · ¿Cuántas mujeres y hombres hay y cuál es la renuncia por género?",
    """
    SELECT
        Gender                                   AS genero,
        COUNT(*)                                 AS total,
        SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END) AS attrition_yes,
        SUM(CASE WHEN Attrition='No'  THEN 1 ELSE 0 END) AS attrition_no
    FROM Clasificacion
    GROUP BY Gender
    ORDER BY Gender
    """,
    ["Género", "Total", "Attrition Yes", "Attrition No"]
)

# ── Q9: JobLevel promedio por nivel educativo ─
ejecutar(
    "Q9 · ¿Cuál es el JobLevel promedio dentro de cada nivel educativo?",
    """
    SELECT
        CASE Education
            WHEN 1 THEN '1 - Below College'
            WHEN 2 THEN '2 - College'
            WHEN 3 THEN '3 - Bachelor'
            WHEN 4 THEN '4 - Master'
            WHEN 5 THEN '5 - Doctor'
        END                         AS nivel_educativo,
        ROUND(AVG(JobLevel), 2)     AS job_level_promedio
    FROM Clasificacion
    GROUP BY Education
    ORDER BY Education
    """,
    ["Nivel Educativo", "JobLevel Promedio"]
)

# ── Q10: Conteo y Attrition por JobSatisfaction ──
ejecutar(
    "Q10 · ¿Cuántas personas hay por nivel de JobSatisfaction y cuántos tienen Attrition Yes/No?",
    """
    SELECT
        CASE JobSatisfaction
            WHEN 1 THEN '1 - Low'
            WHEN 2 THEN '2 - Medium'
            WHEN 3 THEN '3 - High'
            WHEN 4 THEN '4 - Very High'
        END                                      AS satisfaccion_trabajo,
        COUNT(*)                                 AS total,
        SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END) AS attrition_yes,
        SUM(CASE WHEN Attrition='No'  THEN 1 ELSE 0 END) AS attrition_no
    FROM Clasificacion
    GROUP BY JobSatisfaction
    ORDER BY JobSatisfaction
    """,
    ["Satisfacción en el Trabajo", "Total", "Attrition Yes", "Attrition No"]
)

# ── Q11: Conteo y Attrition por MaritalStatus ─
ejecutar(
    "Q11 · ¿Cuántas personas hay por estado civil y cuántos tienen Attrition Yes/No?",
    """
    SELECT
        MaritalStatus                            AS estado_civil,
        COUNT(*)                                 AS total,
        SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END) AS attrition_yes,
        SUM(CASE WHEN Attrition='No'  THEN 1 ELSE 0 END) AS attrition_no
    FROM Clasificacion
    GROUP BY MaritalStatus
    ORDER BY MaritalStatus
    """,
    ["Estado Civil", "Total", "Attrition Yes", "Attrition No"]
)

# ── Q12: Attrition Yes con NumCompaniesWorked >= 2 ──
ejecutar(
    "Q12 · ¿Cuántas personas con Attrition Yes han trabajado en 2 o más empresas (NumCompaniesWorked >= 2)?",
    """
    SELECT COUNT(*) AS total
    FROM Clasificacion
    WHERE Attrition = 'Yes'
      AND NumCompaniesWorked >= 2
    """,
    ["Total (Attrition Yes y NumCompaniesWorked ≥ 2)"]
)

# ── Q13: Conteo y Attrition por Over18 ────────
ejecutar(
    "Q13 · ¿Cuántas personas hay por categoría de Over18 y cuántos tienen Attrition Yes/No?",
    """
    SELECT
        Over18                                   AS mayor_de_18,
        COUNT(*)                                 AS total,
        SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END) AS attrition_yes,
        SUM(CASE WHEN Attrition='No'  THEN 1 ELSE 0 END) AS attrition_no
    FROM Clasificacion
    GROUP BY Over18
    ORDER BY Over18
    """,
    ["Mayor de 18", "Total", "Attrition Yes", "Attrition No"]
)

# ── Q14a: Conteo y Attrition por PerformanceRating ──
ejecutar(
    "Q14a · ¿Cuántas personas hay por PerformanceRating y cuántos tienen Attrition Yes/No?",
    """
    SELECT
        CASE PerformanceRating
            WHEN 1 THEN '1 - Low'
            WHEN 2 THEN '2 - Good'
            WHEN 3 THEN '3 - Excellent'
            WHEN 4 THEN '4 - Outstanding'
        END                                      AS performance_rating,
        COUNT(*)                                 AS total,
        SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END) AS attrition_yes,
        SUM(CASE WHEN Attrition='No'  THEN 1 ELSE 0 END) AS attrition_no
    FROM Clasificacion
    GROUP BY PerformanceRating
    ORDER BY PerformanceRating
    """,
    ["Performance Rating", "Total", "Attrition Yes", "Attrition No"]
)

# ── Q14b: Conteo y Attrition por RelationshipSatisfaction ──
ejecutar(
    "Q14b · ¿Cuántas personas hay por RelationshipSatisfaction y cuántos tienen Attrition Yes/No?",
    """
    SELECT
        CASE RelationshipSatisfaction
            WHEN 1 THEN '1 - Low'
            WHEN 2 THEN '2 - Medium'
            WHEN 3 THEN '3 - High'
            WHEN 4 THEN '4 - Very High'
        END                                      AS satisfaccion_relaciones,
        COUNT(*)                                 AS total,
        SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END) AS attrition_yes,
        SUM(CASE WHEN Attrition='No'  THEN 1 ELSE 0 END) AS attrition_no
    FROM Clasificacion
    GROUP BY RelationshipSatisfaction
    ORDER BY RelationshipSatisfaction
    """,
    ["Satisfacción en Relaciones", "Total", "Attrition Yes", "Attrition No"]
)

# ── Q15: Promedio de MonthlyIncome por StandardHours ──
ejecutar(
    "Q15 · ¿Cuál es el promedio de MonthlyIncome por cada valor de StandardHours?",
    """
    SELECT
        StandardHours                       AS standard_hours,
        ROUND(AVG(MonthlyIncome), 2)        AS promedio_monthly_income,
        COUNT(*)                            AS total_empleados
    FROM Clasificacion
    GROUP BY StandardHours
    ORDER BY StandardHours
    """,
    ["Standard Hours", "Promedio MonthlyIncome", "Total Empleados"]
)

# ── Q16: Attrition Yes con más de 2 años (variables de años) ──
ejecutar(
    "Q16 · ¿Cuántas personas con Attrition Yes tienen más de 2 años en cada variable de antigüedad?",
    """
    SELECT
        SUM(CASE WHEN Attrition='Yes' AND YearsAtCompany         > 2 THEN 1 ELSE 0 END) AS years_at_company_gt2,
        SUM(CASE WHEN Attrition='Yes' AND YearsInCurrentRole     > 2 THEN 1 ELSE 0 END) AS years_in_current_role_gt2,
        SUM(CASE WHEN Attrition='Yes' AND YearsSinceLastPromotion > 2 THEN 1 ELSE 0 END) AS years_since_last_promo_gt2,
        SUM(CASE WHEN Attrition='Yes' AND YearsWithCurrManager   > 2 THEN 1 ELSE 0 END) AS years_with_curr_manager_gt2
    FROM Clasificacion
    """,
    [
        "Attrition Yes & YearsAtCompany > 2",
        "Attrition Yes & YearsInCurrentRole > 2",
        "Attrition Yes & YearsSinceLastPromotion > 2",
        "Attrition Yes & YearsWithCurrManager > 2"
    ]
)

# ─────────────────────────────────────────────
conn.close()
print("\n" + "=" * 60)
print("  ✔ Todas las consultas ejecutadas correctamente.")
print("  ✔ Conexión a la base de datos cerrada.")
print("=" * 60)