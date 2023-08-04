"""
Django settings for medicnewsblog project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
#### We must add these in order to use the environment variables being set 
from environs import Env
env=Env()
env.read_env()



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = 'django-insecure-i7hum1%z_-d-(x#b(6bk#=3wlz0pc-5=q^e3yp*#7!^pbz0yf#'
#### In Production, the secret key is going to change as we get it from the environment variables 
SECRET_KEY=env.str("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True   ###For production purpose note that 

#DEBUG=FALSE , so django can display standard 404 errors when needed

#Moreso we can use our environmenr files instead hence, 
## During production, its appropriate to have a code as below 
###DEBUG=env.bool("DEBUG",default=FALSE)  ##It means if DEBUG is not found, the it should be false, hence we are in development


ALLOWED_HOSTS = []  #### During production these must be set 
###Production Purpose 
### ALLOWED_HOSTS=['herokuapp.com','localhost','127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'medicblog',
    'accounts',
    'pages' #To control some general static pages like Home page, About Section ets
   # 'crispy_forms'  #This allows for smoother styling with bootstrap 4
   # 'whitenoise.runserver_nostatic' ### This is needed since django
   # may not serve static files in production or to make the 
   # weight be thrown off it
   
   
    
    
    
    
    
]
#CRISPY_TEMPLATE_PACK='bootstrap4'
#We want a CustomUser authentication
AUTH_USER_MODEL='accounts.CustomUser'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'whitenoise.middleware.WhiteNoiseMiddleware', #####whitenoise middleware configuration 
]

ROOT_URLCONF = 'medicnewsblog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR.joinpath('templates'))], #This is used to configure our template/html file
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'medicnewsblog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

### During Production the databases will change depending on which database we are using 
"""
DATABASES={
    "default":env.dj_db_url("DATABASE_URL")
    
}

"""


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/' 
#Django simply checks this folder to serve static files during development
#In Django, if you don't specify custom settings for serving static files, 
# the default behavior is to serve CSS files 
# and other static files from the STATIC_URL you've defined in your settings.py file.
STATICFILES_DIRS=[

##This directory sorts of collects all the parts where static is and css or js files served from it
##It often has several options
##example 1: os.path.join(BASE_DIR, 'myapp1', 'static'), 
## example 2: os.path.join(BASE_DIR, 'myapp2', 'static'),

#myproject/
#|-- myapp/
#|   |-- static/
#|   |   |-- css/
#|   |   |   |-- style.css
#|   |   |-- js/
#|   |   |   |-- script.js
#|-- bootstrap/
#|   |-- css/
#|   |   |-- bootstrap.min.css
#|   |-- js/
#|   |   |-- bootstrap.min.js
#|-- myproject/
#|   |-- settings.py
#|-- manage.py

#Imagine a project structure like this 
#1. You need to include bootstrap into the statiffiles_dirs if you need css file from there
# os.path.join(BASE_DIR, 'bootstrap'), #something like this, in this way django treats bootstrap just as static
#and in your html file, you can use a like to get any css file from bootstrap as seen below
# <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">

   str(BASE_DIR.joinpath('static'))
    ]
#STATIC_ROOT is a setting in Django that defines the absolute filesystem path to 
#the directory where Django collects all the static files from 
#your various apps when you run the collectstatic management command. 
#This setting is used in production to store all the static files in a single location,
#which can then be served efficiently by your web server 
#(e.g., Nginx, Apache) or content delivery network (CDN) in a production environment.

STATIC_ROOT=str(BASE_DIR.joinpath('static_root')) #This is mainly important for production use actually for easy serving of files and caching 
#Consolidation and Organizing Assets: The collectstatic command gathers i.e python manage.py collectstatic
#all static files from the individual app static directories and 
#the project-level static directory, if defined in STATICFILES_DIRS, 
#and places them into a single directory defined by STATIC_ROOT.
#This consolidation ensures that all
#static files are organized and served efficiently in a production environment.
STATICFILES_STORAGE='django.contrib.staticfiles.storage.StaticFilesStorage'
#To use Whitenoise instead for production purpose to server static files  ?
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

#After running the python manage.py collectstatic 
# The  development setup of static files actually remains unaffected 
# when you run collectstatic. Django will continue to serve static files 
# as usual from their original locations during development, while the 
# collectstatic command is specifically intended 
# to prepare your project for production.  
######### What the python manage.py collectstatic does ###########  
# Copy all static files from each app's static directory.
#Copy all static files from any additional directories specified in STATICFILES_DIRS.
#Place the collected static files into the directory specified by STATIC_ROOT.

#Media Files Configuration 
MEDIA_URL='/media/'
#MEDIA_ROOT is a setting in Django that specifies the absolute filesystem path 
# to the directory where user-uploaded media files
# (e.g., images, videos, documents) are stored. When a user uploads a file through a Django form 
# or any other means, it gets stored in the directory specified by MEDIA_ROOT.
MEDIA_ROOT=os.path.join(BASE_DIR,'media')



# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL='home' #This is coming due to django.contrib.auth.urls added to the urls.py of the root
LOGOUT_REDIRECT_URL='home'  #Login, logout are singlehanded handed by django.contrib.auth.urls and the registration templates
#Signup is what we need a new accounts app for essentially 


#This email configuration is for the purpose of password reset

EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend'