from django.contrib import admin
from models import *

def nombre_completo(obj):
	return obj.nombre


class AlumnoAdmin(admin.ModelAdmin):
	list_display = (nombre_completo, 'telefono', 'email')
	nombre_completo.admin_order_field = 'nombre'
admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Diagnostico)
admin.site.register(Antecedente)

# Register your models here.
