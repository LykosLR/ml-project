# Documentación datos para proyecto de regresión.

## Nombre de la base de datos
La base de datos original lleva por nombre "IUBAT_Student_Performance_Dataset"

## Fuente (URL)
https://data.mendeley.com/datasets/ns87rtkv58/2

## Descripción general del problema
A partir de información sobre intereses personales, tiempo y métodos de estudios, además de factores de riesgo como las redes sociales o problemas de salud, discapacidades, suspensiones y otras variables personales como ingresos familiares, nivel de inglés, vida social y personal. Se busca analizar el promedio semestral de estudiantes de IUBAT; Una universidad en Bangladesh, además también se analizará su promedio acumulado. El problema es determinar si hay alguna correlación entre estas variables y el desempeño académico de un estudiante.

## Objetivo del análisis
El objetivo es intentar a partir de los datos mencionados anteriormente, ser capaz de predecir el desempeño académico de un estudiante.

## Variable objetivo 
CGPA, promedio acumulado del estudiante, una variable numérica continua.

## Diccionario de variables

### Id (0)
 - *Descripción*: Identificador único asignado a cada estudiante dentro del conjunto de datos.
 - *Tipo de variable*: Identificador (variable nominal sin significado analítico)


### University Admission year
 - *Descripción*: Año en el que el estudiante ingresó a la universidad.
 - *Tipo de variable*: Numérica discreta


### Gender
 - *Descripción*: Género con el que se identifica el estudiante.
 - *Tipo de variable*: Categórica nominal


### Age (Years)
 - *Descripción*: Edad del estudiante expresada en años.
 - *Tipo de variable*: Numérica discreta


### H.S.C passing year
 - *Descripción*: Año en el que el estudiante finalizó la educación secundaria (High School Certificate).
 - *Tipo de variable*: Numérica discreta


### Program
 - *Descripción*: Programa académico o carrera universitaria en la que está matriculado el estudiante.
 - *Tipo de variable*: Categórica nominal


### Current Semester
 - *Descripción*: Semestre académico actual que está cursando el estudiante.
 - *Tipo de variable*: Numérica discreta


### Do you have meritorious scholarship ?
 - *Descripción*: Indica si el estudiante posee una beca otorgada por mérito académico.
 - *Tipo de variable*: Categórica binaria


### Do you use University transportation?
 - *Descripción*: Indica si el estudiante utiliza el servicio de transporte proporcionado por la universidad.
 - *Tipo de variable*: Categórica binaria


### How many hour do you study daily? (Hours )
 - *Descripción*: Número promedio de horas que el estudiante dedica diariamente al estudio.
 - *Tipo de variable*: Numérica discreta


### How many times do you seat for study in a day?
 - *Descripción*: Número de sesiones de estudio que realiza el estudiante durante un día.
 - *Tipo de variable*: Numérica discreta


### What is your preferable learning mode?
 - *Descripción*: Modalidad de aprendizaje preferida por el estudiante (por ejemplo presencial, virtual o autodidacta).
 - *Tipo de variable*: Categórica nominal


### Do you use smart phone?
 - *Descripción*: Indica si el estudiante posee o utiliza un teléfono inteligente.
 - *Tipo de variable*: Categórica binaria


### Do you have personal Computer?
 - *Descripción*: Indica si el estudiante dispone de un computador personal para sus actividades académicas.
 - *Tipo de variable*: Categórica binaria


### How many hour do you spent daily in social media? (Hours)
 - *Descripción*: Cantidad de horas diarias que el estudiante dedica al uso de redes sociales.
 - *Tipo de variable*: Numérica discreta


### Status of your English language proficiency
 - *Descripción*: Nivel de dominio del idioma inglés del estudiante.
 - *Tipo de variable*: Categórica ordinal


### Average attendance on class (Percentage )
 - *Descripción*: Porcentaje promedio de asistencia del estudiante a las clases.
 - *Tipo de variable*: Numérica continua


### Did you ever fall in probation?
 - *Descripción*: Indica si el estudiante ha estado alguna vez en período de prueba académica por bajo rendimiento.
 - *Tipo de variable*: Categórica binaria


### Did you ever got suspension?
 - *Descripción*: Indica si el estudiante ha recibido alguna suspensión académica o disciplinaria.
 - *Tipo de variable*: Categórica binaria


### Do you attend in teacher consultancy for any kind of academical problems?
 - *Descripción*: Indica si el estudiante consulta a profesores para resolver dificultades académicas.
 - *Tipo de variable*: Categórica binaria


### What are the skills do you have ?
 - *Descripción*: Habilidades adicionales que posee el estudiante como programación, liderazgo o comunicación.
 - *Tipo de variable*: Categórica nominal


### How many hour do you spent daily on your skill development? (Hours )
 - *Descripción*: Número de horas diarias que el estudiante dedica al desarrollo de habilidades personales o profesionales.
 - *Tipo de variable*: Numérica discreta


### What is you interested area?
 - *Descripción*: Área principal de interés del estudiante como tecnología, investigación, negocios o arte.
 - *Tipo de variable*: Categórica nominal


### What is your relationship status?
 - *Descripción*: Estado sentimental del estudiante como soltero, en relación o casado.
 - *Tipo de variable*: Categórica nominal


### Are you engaged with any co-curriculum activities?
 - *Descripción*: Indica si el estudiante participa en actividades extracurriculares o co-curriculares.
 - *Tipo de variable*: Categórica binaria


### With whom you are living with?
 - *Descripción*: Indica con quién vive actualmente el estudiante como familia, amigos o solo.
 - *Tipo de variable*: Categórica nominal


### Do you have any health issues?
 - *Descripción*: Indica si el estudiante presenta algún problema de salud.
 - *Tipo de variable*: Categórica binaria


### What was your previous SGPA?
 - *Descripción*: Promedio de calificaciones obtenido por el estudiante en el semestre anterior.
 - *Tipo de variable*: Numérica continua


### Do you have any physical disabilities?
 - *Descripción*: Indica si el estudiante presenta alguna discapacidad física.
 - *Tipo de variable*: Categórica binaria


### What is your current CGPA?
 - *Descripción*: Promedio acumulado de calificaciones del estudiante hasta el momento.
 - *Tipo de variable*: Numérica continua


### How many Credit did you have completed?
 - *Descripción*: Número total de créditos académicos que el estudiante ha aprobado.
 - *Tipo de variable*: Numérica discreta


### What is your monthly Family Income 
 - *Descripción*: Ingreso económico mensual del núcleo familiar del estudiante.
 - *Tipo de variable*: Numérica continua

 ## Número de observaciones
854

 ## Número de variables
32 incluyendo la columna de identificación

 ## Posibles hipótesis de estudio
 - *1*: Se espera que los estudiantes que tengan más tiempo al día estudiando, menos tiempo en redes sociales y que prefieran los cursos de manera presencial (Por estar expuestos a menos distracciones) obtengan mejores resultados en su desempeño académico.
 - *2*: Se espera que exista una correlación entre la solvencia económica familiar y mejores resultados, además se podría pensar que esta correlación es independiente de la existencia de alguna dispacidad.
 - *3*: Se espera que los estudiantes con problemas de comportamiento evidenciados en suspensiones o llamados de atención tengan peor desempeño.