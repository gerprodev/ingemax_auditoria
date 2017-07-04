from django.conf.urls import url
from django.contrib import admin

from .rest import *
from .views import *


urlpatterns = [
	# API REST
    url(r'^api/registro-peticion/$', RegistroPeticionCreateAPIView.as_view(),
        name='registro_peticion'),
]