from django.contrib import admin

##I added model here
from .models import Spirit
# Register your models here.

##This tells Django's built-in admin panel "here's a model, give me a CRUD UI for it.
admin.site.register(Spirit)


##Migrations are how Django translates your Python model into actual SQL CREATE TABLE statements. Run these in your terminal (venv still active):

##python manage.py makemigrations
##python manage.py migrate

## Need source venv/bin/activate