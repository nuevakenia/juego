from django.urls import path

from core.views import Test1View
from core.views import Login
app_name = "core"
urlpatterns = [
    path("test1/", view=Test1View.as_view(), name="test1_view"),
    #path("calc/", view=CalcView.as_view(), name="calc_view"),
    path('', Login.as_view(), name='login')
]
