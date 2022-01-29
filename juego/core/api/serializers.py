from django.contrib.auth import get_user_model
from rest_framework import serializers
from core.models import Personaje, PersonajeDetalle

User = get_user_model()


class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "name", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"}
        }


class PersonajeDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonajeDetalle
        fields = "__all__"


class PersonajeSerializer(serializers.ModelSerializer):
    detalle = PersonajeDetalleSerializer(required=True)

    class Meta:
        model = Personaje
        fields = "__all__"

    def create(self, validated_data):
        detalle_data = validated_data.pop('detalle')
        pj = PersonajeDetalle.objects.create(**detalle_data)
        validated_data.update({'detalle': pj})
        personaje = Personaje.objects.create(**validated_data)

        return personaje
