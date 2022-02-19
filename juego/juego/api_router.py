from django.urls import path, include
from django.contrib.auth.models import User
from django.urls.conf import re_path
from rest_framework import routers, serializers, viewsets
from core.api.views import (PersonajeViewSet, SeleccionPersonajeViewSet,
                            PersonajeCreateAPIView, PersonajeDetailAPIView)

# Serializers define the API representation.


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register("personajes", SeleccionPersonajeViewSet, basename='personajes')
#router.register("personajes/crear", PersonajeCreateAPIView, basename='personajes_crear')
#router.register("personajes/detalle", PersonajeDetailAPIView, basename='personajes_detalle')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('personajes/crear', PersonajeCreateAPIView.as_view(), name="personajes_crear"),
    path('personajes/detalle', PersonajeDetailAPIView.as_view(), name="personajes_detalle")
]
