
# ID.me Authentication

ID.me authentication and verification starter project using python custom lib.

 - [ID.me](https://www.id.me)
## Installation 

```bash
  python --version
  python -m pip install Django
  pip install mozilla-django-oidc django-environ 
  django-admin startproject idmeapp
  python manage.py startapp auth
  python manage.py runserver
  python manage.py makemigrations
  python manage.py migrate
```
    
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`OIDC_RP_CLIENT_ID`

`OIDC_RP_CLIENT_SECRET`

## Documentation

[Documentation](https://help.id.me/hc/en-us)

