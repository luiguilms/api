from django.contrib import admin

# Register your models here.
from .models import Humedad
from .models import Planta
admin.site.register(Humedad)
admin.site.register(Planta)