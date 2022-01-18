from django.contrib.auth import get_user_model
from core.models import ExtendUser

from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from core.models import Personaje
#from users.models import User
from .serializers import UserSerializer, PersonajeSerializer


class PersonajeViewSet(ListModelMixin, GenericViewSet):
    serializer_class = PersonajeSerializer
    queryset = Personaje.objects.all()


class SeleccionPersonajeViewSet(ListModelMixin, GenericViewSet):
    serializer_class = PersonajeSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Personaje.objects.filter(user=user).select_related('personaje_detalles').values()

        return queryset

    def post(self, request, pk, *args, **kwargs):
        user_pj = ExtendUser.objects.get(pj_seleccionado=pk)
        queryset = ExtendUser.objects.get(r=pk).select_related(
            'personaje_detalles').values().update(pj_seleccionado=user_pj)
        return queryset
