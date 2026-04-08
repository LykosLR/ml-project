# Este script se encarga de ejecutar las consultas SQL para el proyecto de Regresión y guardar los resultados en archivos CSV.

import pandas as pd
import sqlite3
from pathlib import Path

# Crear carpeta data/processed/Regresión si no existe


CSV_PATH = Path(__file__).parent.parent / "data" / "processed"/"database.db"
ruta_base = Path(__file__).parent.parent / "data" / "processed"
ruta_base.mkdir(parents=True, exist_ok=True)

#Conectar a la base de datos
conn= sqlite3.connect(CSV_PATH)


#Consultas SQL
query1= """select 
                count(*) as Población,
                count(case when "Gender" = 'Female' then 1 end) as Mujeres,
                count(case when "Gender" = 'Male' then 1 end) as Hombres,
                count(case when "Do you have personal Computer?" = 'Yes' then 1 end) as Poseen_computadora, 
                count(case when "Did you ever fall in probation?"="Yes" then 1 end) as Rechazados,
                count(case when "Did you ever got suspension?"="Yes" then 1 end) as Suspendidos,
                count(case when "Do you have any health issues?"="Yes" then 1 end) as No_saludables,
                count(case when "Do you have any physical disabilities?"="Yes" then 1 end) as Discapacitados
            from regresion;
        """
query2= """select
                avg("Age (Years)") as Edad_promedio,
                avg("Current Semester") as Semestre_promedio,
                avg("How many hour do you study daily? (Hours )") as Horas_estudio_promedio,
                avg("How many times do you seat for study in a day?") as Veces_estudio_promedio,
                avg("How many hour do you spent daily in social media? (Hours)") as Horas_redes_sociales_promedio,
                avg("Average attendance on class (Percentage )") as Asistencia_promedio,
                avg("What is your current CGPA?") as CGPA_promedio,
                avg("How many Credit did you have completed?") as Creditos_completados_promedio,
                avg("What is your monthly Family Income ") as Ingreso_familiar_promedio
            from regresion;
        """
query3= """ select 
                avg("What is your current CGPA?") as Promedio_CGPA,
                "What is your monthly Family Income " as Ingreso_familiar
            from regresion
            group by Ingreso_familiar
            order by Promedio_CGPA desc; 
        """
query4= """ select
                avg("What is your current CGPA?") as Promedio_CGPA,
                "How many hour do you spent daily in social media? (Hours)" as Horas_redes_sociales
            from regresion
            where "Average attendance on class (Percentage )" >= 70 and "What is your preferable learning mode?" = 'Offline'
            group by Horas_redes_sociales
            order by Promedio_CGPA desc;
        """
query5= """ select
                avg("What is your current CGPA?") as Promedio_CGPA,
                "How many hour do you spent daily in social media? (Hours)" as Horas_redes_sociales
            from regresion
            where "Average attendance on class (Percentage )" < 70 and "What is your preferable learning mode?" = 'Offline'
            group by Horas_redes_sociales
            order by Promedio_CGPA desc;
        """

queries = {
    1: query1,
    2: query2,
    3: query3,
    4: query4,
    5: query5
}

numero = int(input("Ingrese el número de la query: "))

if numero not in queries:
    print("Query no válida")
else:
    df = pd.read_sql_query(queries[numero], conn)
    ruta = ruta_base / f'regresion_query{numero}.csv'
    df.to_csv(ruta, index=False)
    print("Archivo guardado")

#Cerrar la conexión
conn.close()

print("Conexión cerrada correctamente.")