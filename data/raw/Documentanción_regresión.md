# Documentación sobre el proyecto de Regresión.

## Nombre de la base de datos.
La base de datos original lleva por nombre "IUBAT_students_performace_Dataset"

## Fuente (URl)
https://data.mendeley.com/datasets/ns87rtkv58/2

## Descripción del problema.
La vida universitaria de una persona está marcada por diversas situaciones y problemas constantes que pueden afectar, de manera positiva o negativa, el desempeño académico de cada estudiante. Por ello, se estudiarán distintos tipos de información relacionados con su vida universitaria, tales como intereses personales, tiempo de estudio, métodos de aprendizaje, acceso a la tecnología, problemas de salud, suspensiones, ingresos familiares y vida social, entre otros.

## Objetivo del análisis
Determinar si existe una correlación entre estas variables y el rendimiento académico de cada estudiante, con el fin de analizar cómo los distintos factores relacionados con la vida universitaria pueden influir en su desempeño académico. A través de este análisis, se busca identificar posibles relaciones entre dichas variables y establecer si algunas de ellas están asociadas de manera significativa con mejores o peores resultados académicos. De esta manera, se pretende comprender mejor qué aspectos del entorno y las condiciones personales de los estudiantes podrían estar vinculados con su rendimiento académico.

## Variable objetivo
CGPA, promedio acomulado del estudiante, una variable numérica continua.

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
 - *Posibles datos*: Programming, Software Development, Web Development (Frontend), Web Development (Backend), Cyber Security, Networking, Content Creation / Writing, Digital Marketing, Graphic Design, Photography / Videography, Video Editing, Animation (2D/3D), Machine Learning, Artificial Intelligence, Data Entry / Data Collection, SEO, App / Android Development, Game Development, UI / UX Design, WordPress, IoT, System Analysis, Market Analysis, Teaching / Mentoring, Problem Solving, MIS (Management Information Systems), JavaScript / PHP (tecnologías específicas) 
 - *Nota*: Algunas respuestas son no válidas o tienen errores tipográficos.
### How many hour do you spent daily on your skill development? (Hours )
 - *Descripción*: Número de horas diarias que el estudiante dedica al desarrollo de habilidades personales o profesionales.
 - *Tipo de variable*: Numérica discreta


### What is you interested area?
 - *Descripción*: Área principal de interés del estudiante como tecnología, investigación, negocios o arte.
 - *Tipo de variable*: Categórica nominal
 - *Posibles datos*:Software Development, Hardware, Networking, Web Development, Machine Learning / Deep Learning, Artificial Intelligence, Data Science, UI / UX Design, Cyber Security, Blockchain / Blockchain Engineering, App Development, Game Development, Graphics Design, Digital Marketing, MIS (Management Information Systems), Physics, Mathematics, QA / Testing, Problem Solving, Competitive Programming, IoT (Internet of Things), Cyber Forensics / Security Analysis
 - *Nota*: En esta pregunta se presenta ruido en forma de respuestas vagas, respuestas narradas y respuestas como "Confuse" 


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
 - *1*: La primera hipótesis es que el nivel de atención de un estudiante se relacione positivamente con su promedio acumulado, para esto buscamos estudiar si los estudiantes que tienen más tiempo al día estudiando, menos tiempo en redes sociales y que prefieren los cursos de manera presencial (Por estar expuestos a menos distracciones) obtienen mejores resultados en su desempeño académico.
 - *2*: En la segunda hipótesis buscamos que exista una correlación entre la solvencia económica familiar y mejores resultados, además se podría pensar que esta correlación es independiente de la existencia de alguna dispacidad.
 - *3*: Para la última hipótesis buscamos encontrar si verdaderamente los estudiantes con problemas de comportamiento evidenciados en suspensiones o llamados de atención tienen peor desempeño, o si por el contrario, su comportamiento es independiente a su rendimiento académico.