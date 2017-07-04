from django.contrib import admin

from .models import RegistroPeticion


class RegistroPeticionAdmin(admin.ModelAdmin):
    list_filter = ('instancia', 'tipo_peticion', 'codigo_peticion',
        'importante', 'solucionado')
    list_display = ['instancia', 'tipo_peticion', 'codigo_peticion', 'url',
        'get_usuario', 'fecha_acceso', 'importante', 'solucionado']

admin.site.register(RegistroPeticion, RegistroPeticionAdmin)