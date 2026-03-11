# Documentación datos para proyecto de regresión.

## Nombre de la base de datos
El conjunto de datos original lleva como nombre "WA_Fn-UseC_-HR-Employee-Attrition.csv"


## Fuente (URL)
https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset

## Descripción general del problema
De un conjunto de trabajadores de una empresa, se consultan una serie de datos de índole demográfico, académico, personal y de riesgos psicosociales en el trabajo, y se añade la variable de si el trabajador ha renunciado o no a su empleo. El problema es intentar encontrar alguna relación entre las variables y la renuncia de los trabajores con el fin de intentar reducir este indicador dentro de la empresa y así poder mantener a los trabajadores con mejores condiciones laborales y reducir costos en inducciones.

## Objetivo del análisis
Intentar determinar solo con las variables solicitadas si un trabajador es propenso o no a renunciar a su empleo, para poder identificarlos y reducir ese riesgo.

## Variable objetivo 
Attrition (Rotación de personal en la empresa)

## Diccionario de variables


### Age
 - *Descripción*: Edad del empleado expresada en años.
 - *Tipo de variable*: Numérica discreta


### Attrition
 - *Descripción*: Indica si el empleado ha dejado la empresa o continúa trabajando en ella.
 - *Tipo de variable*: Categórica binaria


### BusinessTravel
 - *Descripción*: Frecuencia con la que el empleado debe viajar por motivos laborales.
 - *Tipo de variable*: Categórica ordinal


### DailyRate
 - *Descripción*: Tarifa o ingreso diario asociado al empleado.
 - *Tipo de variable*: Numérica continua


### Department
 - *Descripción*: Departamento de la empresa en el que trabaja el empleado.
 - *Tipo de variable*: Categórica nominal


### DistanceFromHome
 - *Descripción*: Distancia aproximada entre la residencia del empleado y su lugar de trabajo.
 - *Tipo de variable*: Numérica discreta


### Education
 - *Descripción*: Nivel educativo alcanzado por el empleado según una escala establecida.
 - *Tipo de variable*: Numérica discreta
    -1 'Below College' 
    -2 'College' 
    -3 'Bachelor' 
    -4 'Master' 
    -5 'Doctor'


### EducationField
 - *Descripción*: Área o campo académico en el que el empleado realizó sus estudios.
 - *Tipo de variable*: Categórica nominal


### EmployeeCount
 - *Descripción*: Número de empleados registrados; suele ser constante para todos los registros.
 - *Tipo de variable*: Numérica discreta


### EmployeeNumber
 - *Descripción*: Identificador único asignado a cada empleado dentro de la empresa.
 - *Tipo de variable*: Identificador (variable nominal sin significado analítico)


### EnvironmentSatisfaction
 - *Descripción*: Nivel de satisfacción del empleado con su entorno laboral.
 - *Tipo de variable*: Numérica discreta
    -1 'Low' 
    -2 'Medium' 
    -3 'High' 
    -4 'Very High'


### Gender
 - *Descripción*: Género del empleado.
 - *Tipo de variable*: Categórica nominal


### HourlyRate
 - *Descripción*: Tarifa de pago por hora asociada al empleado.
 - *Tipo de variable*: Numérica continua


### JobInvolvement
 - *Descripción*: Nivel de implicación o compromiso del empleado con su trabajo.
 - *Tipo de variable*: Numérica discreta
    -1 'Low' 
    -2 'Medium' 
    -3 'High' 
    -4 'Very High'


### JobLevel
 - *Descripción*: Nivel jerárquico del puesto que ocupa el empleado dentro de la organización.
 - *Tipo de variable*: Categórica ordinal


### JobRole
 - *Descripción*: Cargo o rol específico que desempeña el empleado en la empresa.
 - *Tipo de variable*: Categórica nominal


### JobSatisfaction
 - *Descripción*: Nivel de satisfacción del empleado con su trabajo.
 - *Tipo de variable*: Numérica discreta
    -1 'Low' 
    -2 'Medium' 
    -3 'High' 
    -4 'Very High'


### MaritalStatus
 - *Descripción*: Estado civil del empleado.
 - *Tipo de variable*: Categórica nominal


### MonthlyIncome
 - *Descripción*: Ingreso mensual que recibe el empleado.
 - *Tipo de variable*: Numérica continua


### MonthlyRate
 - *Descripción*: Tarifa mensual asociada al empleado dentro del sistema de remuneración.
 - *Tipo de variable*: Numérica continua


### NumCompaniesWorked
 - *Descripción*: Número de empresas en las que el empleado ha trabajado previamente.
 - *Tipo de variable*: Numérica discreta


### Over18
 - *Descripción*: Indica si el empleado es mayor de 18 años.
 - *Tipo de variable*: Categórica binaria


### OverTime
 - *Descripción*: Indica si el empleado realiza horas extra en su trabajo.
 - *Tipo de variable*: Categórica binaria


### PercentSalaryHike
 - *Descripción*: Porcentaje de aumento salarial que recibió el empleado en la última revisión.
 - *Tipo de variable*: Numérica continua


### PerformanceRating
 - *Descripción*: Calificación del desempeño laboral del empleado según evaluaciones internas.
 - *Tipo de variable*: Numérica discreta
    -1 'Low' 
    -2 'Good' 
    -3 'Excellent' 
    -4 'Outstanding'


### RelationshipSatisfaction
 - *Descripción*: Nivel de satisfacción del empleado con sus relaciones laborales dentro de la empresa.
 - *Tipo de variable*: Numérica discreta
    -1 'Low' 
    -2 'Medium' 
    -3 'High' 
    -4 'Very High'


### StandardHours
 - *Descripción*: Número estándar de horas laborales establecidas por la empresa.
 - *Tipo de variable*: Numérica discreta


### StockOptionLevel
 - *Descripción*: Nivel de beneficios en opciones de acciones otorgadas al empleado.
 - *Tipo de variable*: Categórica ordinal


### TotalWorkingYears
 - *Descripción*: Número total de años de experiencia laboral acumulada por el empleado.
 - *Tipo de variable*: Numérica discreta


### TrainingTimesLastYear
 - *Descripción*: Número de veces que el empleado participó en capacitaciones durante el último año.
 - *Tipo de variable*: Numérica discreta


### WorkLifeBalance
 - *Descripción*: Nivel percibido de equilibrio entre la vida personal y laboral del empleado.
 - *Tipo de variable*: Numérica discreta
    -1 'Bad'
    -2 'Good' 
    -3 'Better' 
    -4 'Best'


### YearsAtCompany
 - *Descripción*: Número de años que el empleado ha trabajado en la empresa actual.
 - *Tipo de variable*: Numérica discreta


### YearsInCurrentRole
 - *Descripción*: Número de años que el empleado ha permanecido en su puesto actual.
 - *Tipo de variable*: Numérica discreta


### YearsSinceLastPromotion
 - *Descripción*: Número de años transcurridos desde la última promoción del empleado.
 - *Tipo de variable*: Numérica discreta


### YearsWithCurrManager
 - *Descripción*: Número de años que el empleado ha trabajado bajo la supervisión de su actual gerente.
 - *Tipo de variable*: Numérica discreta


 ## Número de observaciones
1470

 ## Número de variables
35 contando el identificador

 ## Posibles hipótesis de estudio
 - *1*: Se espera que en una empresa con una buena gestión de seguridad y salud en el trabajo, las calificaciones de los empleados y su percepción de la empresa se relacionen tanto con no renunciar como con un buen salario.
 - *2*: Se espera que en los casos donde la persona tiene un estilo de vida desorganizado o con malas relaciones personales, sea más propenso a tener peores calificaciones y a dejar su empleo.
 - *3*: Se espera que las personas jóvenes o un estudio de nivel universitario sean más propensas a renunciar en búsqueda de mejores oportunidades.