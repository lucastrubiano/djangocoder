# djangocoder
En este repo van a encontrar el proyecto completo de Django


Instalar django

```shell
python -m pip install django
```

Aplicar cambios en base de datos

```shell
python manage.py makemigrations
python manage.py migrate
```

Iniciar servidor

```shell
python manage.py runserver
```

Crear usuario administrador

```shell
python manage.py createsuperuser
```
---
## Deploy en Heroku

Para hacer el despliegue de esta app en heroku debemos seguir los siguientes pasos:

1. Instalar las siguientes bibliotecas:
    - dj-database-url
    - gunicorn
    - whitenoise
    - psycopg2
    - Nota: todo esto está dentro del `requirements.txt`
2. asd 

```shell
heroku create
git push heroku master
```