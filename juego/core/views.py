from django.shortcuts import render
from django.views.generic import TemplateView

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from core.api.serializers import UserTokenSerializer
# Create your views here.


class Login(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data=request.data, context={'request': request})
        #print("LOGIN SERIALIZER", login_serializer)
        if login_serializer.is_valid():
            #print("Paso la validación: ", login_serializer.validated_data['user'])
            user = login_serializer.validated_data['user']
            if user.is_active:
                print("activado")
                token, created = Token.objects.get_or_create(user=user)
                user_serializer = UserTokenSerializer(user)
                print("USER DATA: ", user_serializer.data)
                print("TOKEN: ", created)
                print()
                tok = token
                if created:

                    return Response({
                        'token': token.key,
                        'user': user_serializer.data,
                        'message': 'Inicio de sesión exitoso'
                    }, status=status.HTTP_201_CREATED)
                else:
                    token.delete()
                    token = Token.objects.create(user=user)
                    print("NO CREADO")
            else:
                return Response({'error': 'Este usuario no puede iniciar sesión'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error': 'Nombre de usuario o contraseña incorrectos'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response({'mensaje': 'Hola desde response'}, status=status.HTTP_200_OK)

class Test1View(TemplateView):

    template_name = "test1.html"

    def get(self, request):

        return render(request, "test1.html")

    def post(self, request):
        #usuaios = User.objects.filter(groups__name='')
        return render(request, "home.html")


test1_view = Test1View.as_view()

class Test1View(TemplateView):

    template_name = "test1.html"

    def get(self, request):

        return render(request, "test1.html")

    def post(self, request):
        #usuaios = User.objects.filter(groups__name='')
        return render(request, "home.html")


test1_view = Test1View.as_view()


class CalcView(TemplateView):

    template_name = "calc.html"

    def get(self, request):

        return render(request, "calc.html")

    def post(self, request):
        #usuaios = User.objects.filter(groups__name='')
        return render(request, "calc.html")


calc_view = CalcView.as_view()


class FrontendRenderView(TemplateView):

    template_name = "front.html"

    def get(self, request):

        return render(request, "front.html")

    def post(self, request):
        #usuaios = User.objects.filter(groups__name='')
        return render(request, "front.html")


frontendRender_view = FrontendRenderView.as_view()
