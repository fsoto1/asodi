# Sistema de registro de socios de Asodi

##  Descripción
Desarrollo enfocado a resolver las necesidades de la Asociación de Dializados y Transplantados de Chile (Asodi) por tener un sistema que administre los socios y su respectivo pago de cuotas. Y utilizado como proyecto de asignatura para **Desarrollo Web** y **Seguridad de la Información**.

##  Características

Basado en Django Framework, contiene las siguientes funcionalidades

  - Administrador de Socios
  - Administrador de Apoderados
  - Administrador de Centros de Salud
  - Reportería de datos
  - Administración de Cuotas de Socios
  - Panel de administrador
  - Generador de Citaciones
  - Generador de Credencial de Socios




### Tecnologías

Se combinan distintos proyectos open source:

* [Django](https://www.djangoproject.com/) - Framework para el desarrollo web basado en Python
* [Bootstrap](http://getbootstrap.com/) - HTML, CSS y JS Responsive Framework
* [jQuery](http://jquery.com/)  - Librería JS
* [GitHub](https://github.com) - Versionamiento de código


### Instalación

Testeado en ambientes con Python 3.6.2

Comandos relevantes para ejecutar el sistema

```sh
$ git clone git@github.com:fsoto1/asodi.git
$ pip install -r requirements.txt
```

### Credenciales
Este sitio cuenta con permisos de usuario, se han definido dos usuarios para la navegación:

* **Administrador**
Tiene acceso a todas las páginas del sitio
Usuario: **admin**
Contraseña: **admin123**
* **Usuario**
Tiene un limitado acceso a las páginas del sitio y no puede acceder al administrador de django
Usuario: **usuario**
Contraseña: **user1234**

### Por hacer
* Agregar funcionalidad de subir archivos
* Agregar la aplicación de citaciones
* Agregar la aplicación de Reportería
* Agregar la aplicación de Administración de Cuotas
