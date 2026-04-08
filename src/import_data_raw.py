# Este script se encarga de importar los datos desde los archivos CSV y guardarlos en una base de datos SQLite.

import pandas as pd
import sqlite3
from pathlib import Path

#Crear carpeta database si no existe
Path('database').mkdir(parents=True, exist_ok=True)

# Leer csv


CSV_PATH = Path(__file__).parent.parent / "data" / "raw"
df1= pd.read_csv(CSV_PATH / "dataset_Regresion.csv")
df2= pd.read_csv(CSV_PATH / "dataset_Clasificacion.csv")

# Crear la base de datos dentro de la carpeta database
conn1= sqlite3.connect('database/regresion.db')
conn2= sqlite3.connect('database/clasificacion.db')

# Pasar csv a tabla SQL
df1.to_sql('regresion', conn1, if_exists='replace', index=False)
df2.to_sql('clasificacion', conn2, if_exists='replace', index=False)

# Cerrar la conexión
conn1.close()
conn2.close()

print("Datos importados correctamente a la base de datos.")