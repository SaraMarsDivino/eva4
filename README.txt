Descripción del Proyecto Este proyecto es una aplicación web desarrollada en Django y HTML/CSS/JavaScript para la gestión de estudiantes, profesores y clases. Permite realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) y asignar clases a estudiantes y profesores.

Modelos
Los modelos principales del proyecto son Estudiante, Profesor y Clase, cada uno con sus atributos:

	Estudiante
	id (int): Identificador único.
	nombre (str): Nombre del estudiante.
	correo (str): Correo electrónico del estudiante.
	clases_inscritas (ManyToMany): Clases en las que el estudiante está inscrito.

	Profesor
	id (int): Identificador único.
	nombre (str): Nombre del profesor.
	especialidad (str): Área de especialización del profesor.
	clases_impartidas (ManyToMany): Clases que el profesor imparte.

	Clase
	id (int): Identificador único.
	nombre (str): Nombre de la clase.
	horario (str): Horario de la clase.
	descripcion (str): Descripción de la clase

-Ejemplos de uso de la API 🛠️
A continuación, se describen ejemplos básicos de uso de la API REST para Estudiantes, Profesores y Clases.

Autenticación
La API utiliza Token para la autenticación. Debes incluir el token en los encabezados de cada solicitud:

Crear un recurso
Crear Estudiante: Envía un nombre y un correo para registrar un nuevo estudiante.
Crear Profesor: Proporciona un nombre y una especial dad.
Crear Clase: Define un nombre, horario y descripción de la clase.
Obtener recursos
Puedes obtener listas de Estudiantes, Profesores o Clases usando solicitudes GET.
Los datos incluyen información detallada y relaciones, como clases inscritas en estudiantes o clases impartidas por profesores.





La interfaz está diseñada con una paleta de colores inspirada en League of Legends para una mejor experiencia visual.

Características Principales CRUD Completo: Crear, editar y eliminar estudiantes, profesores y clases. Asignación de Clases: Inscribir estudiantes en clases. Asignar clases a profesores.

Requisitos Previos Asegúrate de tener instalados los siguientes componentes en tu máquina: -Python (v3.8 o superior): Instalar Python -Django (v4.x o superior) -Pip: Sistema de gestión de paquetes para Python. -Git: Control de versiones.

Instalación del Proyecto -Clonar el Repositorio Primero, clona este repositorio usando git: git clone https://github.com/SaraMarsDivino/eva4.git cd eva4

-Crear un Entorno Virtual Crea un entorno virtual para evitar conflictos de dependencias:

-Instalar las Dependencias Instala los paquetes requeridos desde requirements.txt: pip install -r requirements.txt

-Migraciones de Base de Datos Ejecuta las migraciones iniciales para configurar la base de datos: python manage.py makemigrations python manage.py migrate

-Crear un Superusuario Crea un superusuario para acceder al panel de administración de Django: python manage.py createsuperuser Sigue las instrucciones en pantalla para ingresar el nombre de usuario, correo electrónico y contraseña.

-Ejecución del Servidor Inicia el servidor local con el siguiente comando: python manage.py runserver

-Abre tu navegador y visita: http://127.0.0.1:8000/