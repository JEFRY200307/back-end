from django.contrib import admin

from usuarios.models import *

# Register your models here.

admin.site.register(Users)
admin.site.register(Domicilio)