from rest_framework import generics

from .models import RegistroPeticion
from .serializers import RegistroPeticionSerializer


class RegistroPeticionCreateAPIView(generics.CreateAPIView):
    serializer_class = RegistroPeticionSerializer
    queryset = RegistroPeticion.objects.all()