from django.db import models

from django_mysql import models as mysql_models


class RegistroPeticion(models.Model):
    """
    Registro de peticiones, se guarda el usuario(username y pk) que realizo la
    peticion, el nombre de la instancia, la fecha y el tiempo que tarda en
    ejecutarse; Y si la peticion es POST se guarda la informacion.
    """
    instancia = models.CharField(max_length=150)
    usuario_nombre = models.CharField(max_length=150)
    usuario_pk = models.IntegerField()
    url = models.TextField()
    tipo_peticion = models.CharField(max_length=10)
    codigo_peticion = models.IntegerField()
    # Opcionales
    tiempo = models.FloatField(default=0)
    informacion = mysql_models.JSONField(null=True, blank=True)
    errores = models.TextField(blank=True, null=True)
    fecha_acceso = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Registro de peticiones'

    def __str__(self):
    	return '%s (%s - %s(%d))' % (self.instancia, self.tipo_peticion,
    		self.usuario_nombre, self.usuario_pk)