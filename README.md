
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

### VS code steps.

 Click on the search window.
 
 ![Search](https://github.com/wasatchinfotech/idme-fed-auth/blob/main/images/vs1.jpg?raw=true)

 Select Python:Create Environment

 ![Python Selection](https://github.com/wasatchinfotech/idme-fed-auth/blob/main/images/vs2.jpg?raw=true)

 Select Environment Type
 
 ![Virtual Environment](https://github.com/wasatchinfotech/idme-fed-auth/blob/main/images/vs3.jpg?raw=true)

 Python Interpreter version selection.

 ![Python Version](https://github.com/wasatchinfotech/idme-fed-auth/blob/main/images/vs4.jpg?raw=true)

 VS Virtual Environment.
 
 ![Editor Venv](https://github.com/wasatchinfotech/idme-fed-auth/blob/main/images/vs5.jpg?raw=true)
 
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`OIDC_RP_CLIENT_ID`

`OIDC_RP_CLIENT_SECRET`

## Demo

Landing page, click on the link for login.

![Home](https://github.com/wasatchinfotech/idme-fed-auth/blob/main/images/home.jpg?raw=true)

ID.me account login page with credentials.

![Login](https://github.com/wasatchinfotech/idme-fed-auth/blob/main/images/login.jpg?raw=true)

After providing correct credentials this will trigger MFA with registered phone number.

![Phone](https://github.com/wasatchinfotech/idme-fed-auth/blob/main/images/phone.jpg?raw=true)

Enter the code for authentication.

![Code](https://github.com/wasatchinfotech/idme-fed-auth/blob/main/images/code.jpg?raw=true)

After successfully authentication application will show account information page.

![Account Info](https://github.com/wasatchinfotech/idme-fed-auth/blob/main/images/account.jpg?raw=true)


## Documentation

[Documentation](https://help.id.me/hc/en-us)

## Support

For support, email info@wasatchinfotech.com

