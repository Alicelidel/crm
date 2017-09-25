import os
from celery import Celery
from django.conf import settings
#main django settings for celery
#celery knows about project with django-settings-module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')
#making celery class object for the app
app = Celery('myshop')
#pointing to config file
app.config_from_object('django.conf:settings')
#saying which apps use this
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)