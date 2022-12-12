from django.urls import path
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path('registrarse/', views.registrarse, name='signup'),
    # path('ingresar/', views.index, name='login'),
    path('inventario/', views.inventario, name='inventario'),
    path('matronas/', views.matronas, name='matronas'),
    path('buscar/', views.buscar, name='buscar'),
    path('lugar/', views.lugar, name='lugar'),
    path('estado/', views.estado, name='estado'),
]
