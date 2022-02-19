from django.contrib.auth import get_user_model
from core.models import ExtendUser
from core.models import PersonajeDetalle

from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework import generics, status
from rest_framework.generics import ListAPIView
from django.views.generic import CreateView, DetailView, UpdateView
from core.models import Personaje
# from users.models import User
from .serializers import UserSerializer, PersonajeSerializer


class PersonajeViewSet(ListModelMixin, GenericViewSet):
    serializer_class = PersonajeSerializer
    queryset = Personaje.objects.all()


class SeleccionPersonajeViewSet(ListModelMixin, GenericViewSet):
    serializer_class = PersonajeSerializer

    def get_queryset(self):
        #user = self.request.user
        queryset = Personaje.objects.select_related('detalle').filter()
        #print("User: ", user.id)
        return queryset


class PersonajeCreateAPIView(generics.CreateAPIView):
    serializer_class = PersonajeSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Personaje.objects.select_related('detalle').filter(user=user.id)
        print("User: ", user.id)
        return queryset

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Personaje creado exitosamente!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PersonajeDetailAPIView(generics.CreateAPIView):
 
    serializer_class = PersonajeSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Personaje.objects.select_related('detalle').filter(user=user.id)
        print("User: ", user.id)
        return queryset


