from rest_framework import serializers

from .models import RegistroPeticion


class RegistroPeticionSerializer(serializers.ModelSerializer):

    class Meta:
        model = RegistroPeticion
        fields = '__all__'