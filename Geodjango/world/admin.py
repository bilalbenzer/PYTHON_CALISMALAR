from django.contrib import admin

# Register your models here.
from django.contrib.gis import admin
from .models import WorldBorder


admin.site.register(WorldBorder, admin.GISModelAdmin)