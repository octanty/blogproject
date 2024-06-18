# blogproject

To run this project
you should conduct some installations
1. Download python on this link: https://www.python.org/downloads/
2. Run the cmd django-admin startproject blogproject
3. install django restframework by typing this keyword: pip install djangorestframework
4. install app by typing this keyword: djang-admin startapp blogapp
5. Add  'blogapp' in INSTALLED_APPS section in settings.py
6. create some modules on module.py, for user, create CustomUser
7. create folder named api and create files named serializer and __init__.py
8. For authentication, add 'rest_framework_simplejwt.token_blacklist' in INSTALLED_APPS section in settings.py
and Put this below code on that
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}
AUTH_USER_MODEL = 'blogapp.CustomUser'
