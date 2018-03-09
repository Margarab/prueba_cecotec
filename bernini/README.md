# Caso Práctico Zapatos Bernini

## Set Up
Clone repository and install requirements with:

    pip install -r requirements.txt


Go to the repository directory and launch server:

    python manage.py runserver



## Settings
If user and password for gmail are provided, email is sent through gmail. Else, email output is sent to console.

    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = ''
    EMAIL_HOST_PASSWORD = ''
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True

    # if provide credentials, send mail through gmail smtp server
    if EMAIL_HOST_USER != '' and EMAIL_HOST_PASSWORD != '':
        EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'

    # Output email messages for console
    else:
        EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


## Users
> Login as admin

    user: admin  password:p4$$w0rd

User admin have permission to add, edit and delete all objects


> Login as client

    user: client1  password:p4$$w0rd

    user: client2  password:p4$$w0rd

Users client only have permissions to add orders.

## Sitemap
API REST with [Django REST Framework](http://www.django-rest-framework.org/)

    - / : Orders management (User admin and client have different permissions)
    - /api/ : Api ROOT
    - /api/products/ : Product List
    - /api/products/?format=json : Product List in json
    - /admin/ : Users and Products management (Only for user admin)
    - /login/ : Login page

## Comments
> Admin can download orders in csv format from /orders/order/, selecting action 'Download order in CSV'

> Order in csv is attached to email.


