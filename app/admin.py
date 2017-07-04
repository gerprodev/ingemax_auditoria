from django.contrib import admin

from .models import RegistroPeticion


class RegistroPeticionAdmin(admin.ModelAdmin):
    list_filter = ('instancia', 'tipo_peticion', 'codigo_peticion')

admin.site.register(RegistroPeticion, RegistroPeticionAdmin)