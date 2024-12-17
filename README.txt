Descripción del Proyecto Este proyecto es una aplicación web desarrollada en Django y HTML/CSS/JavaScript para la gestión de estudiantes, profesores y clases. Permite realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) y asignar clases a estudiantes y profesores.

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