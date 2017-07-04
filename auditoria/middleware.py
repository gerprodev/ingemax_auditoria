# -*- coding: utf-8 -*-
import time
import json
import traceback

import requests

from django.conf import settings


class ControlPeticionesMiddleware(object):
    """ Middleware para registro de peticiones """

    def __init__(self, get_response):
        self.get_response = get_response
        self.registro_peticion = dict()
        self.headers = {'Content-type': 'application/json'}

    def __call__(self, request):
        tiempo_inicio = time.time()
        response = self.get_response(request)
        if settings.AUDITORIA_EXCLUIR_ANONIMOS and request.user.is_anonymous():
            return response
        if request.get_full_path() in settings.AUDITORIA_EXCLUIR_URLS:
            return response
        if request.method not in settings.AUDITORIA_INCLUIR_METODOS:
            return response
        if response.status_code in settings.AUDITORIA_EXCLUIR_PETICIONES:
            return response
        self.registro_peticion['instancia'] = settings.AUDITORIA_INSTANCIA_ID
        self.registro_peticion['usuario_nombre'] = request.user.username
        self.registro_peticion['usuario_pk'] = request.user.pk
        self.registro_peticion['url'] = request.get_full_path()
        self.registro_peticion['tipo_peticion'] = request.method
        self.registro_peticion['usuario_pk'] = request.user.pk
        if request.method == 'POST':
            self.registro_peticion['informacion'] = json.dumps(request.POST)
        if hasattr(response, 'status_code'):
            self.registro_peticion['codigo_peticion'] = response.status_code
        else:
            self.registro_peticion['codigo_peticion'] = 200
        self.registro_peticion['tiempo'] = time.time() - tiempo_inicio
        try:
            requests.post(settings.AUDITORIA_URL_SERVICIO,
                json=self.registro_peticion, headers=self.headers)
        except:
            pass
        return response

    def process_exception(self, request, exception):
        if self.registro_peticion:
            self.registro_peticion['errores'] = traceback.format_exc()
