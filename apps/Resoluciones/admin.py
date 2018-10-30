from django.contrib import admin
from apps.Resoluciones.models import Operador,Resolucion
# Register your models here.
#Modelo para la manipulacion de datos por medio del Admin
class ResolucionAdmin(admin.ModelAdmin):
    list_display = ('NumeroResolucion','FechaDeAutorizacion','TipoDeDocumento')

class OperadorAdmin(admin.ModelAdmin):
    list_display = ('Nombre', 'Rol')    
#Formateo visual del admin
admin.site.register(Resolucion,ResolucionAdmin)
admin.site.register(Operador,OperadorAdmin)
