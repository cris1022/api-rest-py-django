# Proyecto Django: API REST con Django

## Pasos realizados hasta el momento

### 1. Creación del entorno virtual
```bash
python -m venv envs/my_blog
```

### 2. Activación del entorno virtual
Nos ubicamos en el directorio del entorno virtual y ejecutamos:
```bash
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\Scripts\Activate.ps1
```
Para desactivar el entorno virtual:
```bash
deactivate
```

### 3. Instalación de Django
Instalamos Django en el entorno virtual:
```bash
pip install django
```

### 4. Confirmación de dependencias instaladas
Verificamos las dependencias instaladas:
```bash
pip freeze
```

### 5. Creación de un nuevo proyecto
Creamos un nuevo proyecto llamado `my_blog`:
```bash
django-admin startproject my_blog
```

### 6. Validación de comandos disponibles
Nos ubicamos dentro del proyecto Django y ejecutamos:
```bash
python manage.py help
```

### 7. Ejecución del servidor de desarrollo
Iniciamos el servidor de desarrollo:
```bash
python manage.py runserver
```

### 8. Migraciones iniciales
Ejecutamos las migraciones para crear las tablas de la base de datos:
```bash
python manage.py migrate
```

### 9. Creación de un superusuario
Creamos un superusuario para acceder al panel de administración:
```bash
python manage.py createsuperuser
```
- **Username**: AbondanoCristian
- **Email**: abondano930719@gmail.com
- **Password**: Kristhyn2874#

### 10. Creación de una aplicación para gestionar posts
Creamos una nueva aplicación llamada `posts`:
```bash
python manage.py startapp posts
```

### 11. Registro de la aplicación en `settings.py`
Agregamos la aplicación `posts` en la lista de `INSTALLED_APPS` dentro del archivo `settings.py`.

### 12. Implementación de la primera vista
Creamos una vista de ejemplo en `views.py` dentro de la aplicación `posts` y la registramos en el archivo `urls.py` del proyecto.

### 13. Creación de plantillas (templates)
En la aplicación `posts`, añadimos un nuevo directorio llamado `templates` y creamos un archivo HTML llamado `hello_world.html`. Este archivo se utiliza como plantilla en la vista creada en `views.py` de la aplicación `posts`.

### 14. Creación de modelos para la base de datos
Definimos los modelos de nuestra base de datos en el archivo `models.py` dentro de la aplicación `posts`. Los modelos representan las estructuras de las tablas en la base de datos.

### 15. Creación y ejecución de migraciones
Para reflejar los modelos en la base de datos, seguimos estos pasos:

1. **Crear las migraciones**:
   Ejecutamos el siguiente comando para generar un archivo de migración basado en los modelos definidos:
   ```bash
   python manage.py makemigrations
   ```
   Esto creará una carpeta llamada `migrations` dentro de la aplicación `posts`, que contendrá un archivo Python con las instrucciones necesarias para aplicar los cambios en la base de datos.

2. **Aplicar las migraciones**:
   Ejecutamos el siguiente comando para aplicar los cambios en la base de datos:
   ```bash
   python manage.py migrate
   ```

### 16. Instalación de Django REST Framework
Para crear una API REST, instalamos el framework Django REST Framework dentro del entorno virtual:
```bash
pip install djangorestframework
```

Luego, añadimos `'rest_framework'` a la lista de `INSTALLED_APPS` en el archivo `settings.py` del proyecto `my_blog`.

### 17. Registro del modelo en el panel de administración
Para gestionar el modelo `Post` desde el panel de administración de Django, lo registramos en el archivo `admin.py` de la aplicación `posts`:
```python
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

### 18. Creación de un endpoint para visualizar datos
Dentro de la aplicación `posts`, creamos un nuevo directorio llamado `api` y dentro de este:
1. Creamos un archivo vacío llamado `__init__.py` para que sea reconocido como un módulo.
2. Creamos el archivo `views.py` donde definimos nuestro primer endpoint:

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from posts.models import Post

class PostApiView(APIView):
    def get(self, request):
        posts = [post.title for post in Post.objects.all()]
        return Response(data=posts)
```

### 19. Enrutamiento del endpoint en el proyecto
En el archivo `urls.py` del proyecto `my_blog`, añadimos la ruta para el endpoint:
```python
from django.urls import path
from posts.api.views import PostApiView

urlpatterns = [
    path('api/posts/', PostApiView.as_view(), name='post-api'),
]
```

### 20. Importación del modelo en la vista
En el archivo `views.py` de la aplicación `posts`, importamos el modelo `Post` para interactuar con los datos almacenados en la base de datos.

### 21. Definición de los métodos GET y POST
En el archivo `views.py`, definimos los métodos para manejar las solicitudes HTTP:
- **GET**: Para consultar los datos del modelo `Post`.
- **POST**: Para agregar información al modelo `Post`.

```python
class PostApiView(APIView):
    def get(self, request):
        posts = [post.title for post in Post.objects.all()]
        return Response(data=posts)

    def post(self, request):
        Post.objects.create(
            title=request.data.get('title'),
            description=request.data.get('description'),
            order=request.data.get('order')
        )
        return self.get(request)
```
