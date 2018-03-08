# Caso Práctico Zapatos Bernini

## Set Up
Clone repository and install requirements with:

    pip install -r requirements.txt


Go to the repository directory and launch server:

    python manage.py runserver



## Settings
When DEBUG is True, the email is output to the console. To change this behaviour, change DEBUG to False and provide user and password in email settings

    if DEBUG:
        EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'
    else:
        EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
        EMAIL_HOST = "smtp.gmail.com"
        EMAIL_HOST_USER = ""
        EMAIL_HOST_PASSWORD = ""
        EMAIL_PORT = 587
        EMAIL_USE_TLS = True


## Users
> To login as admin

    user: admin  password:p4$$w0rd

User admin has permission for add, edit and delete all objects


> To login as client

    user: client1  password:p4$$w0rd

    user: client2  password:p4$$w0rd

Users client only has permissions for add orders. Doesn't has permissions to do anything in admin pages.

## Site map
API REST with [Django REST Framework](http://www.django-rest-framework.org/)

    - / : Orders management
    - /api/ : Api ROOT
    - /api/products/ : Product List
    - /api/products/?format=json : Product List in json
    - /admin/ : Site administration


