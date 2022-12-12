from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.generic.base import TemplateView

from . import models


def index(request):
    equipo_list = models.Equipo.objects.order_by('ide')

    template = loader.get_template('inventario.html')
    context = {
        "equipo_list": equipo_list,
    }
    return HttpResponse(template.render(context, request))

def registrarse(request):
    return TemplateView.as_view(template_name="home.html")(request)

def inventario(request):
    equipo_list = models.Equipo.objects.order_by('ide')

    template = loader.get_template('inventario.html')
    context = {
        "equipo_list": equipo_list,
    }
    return HttpResponse(template.render(context, request))


def matronas(request):
    return TemplateView.as_view(template_name="home.html")(request)

def buscar(request):
    return TemplateView.as_view(template_name="home.html")(request)

def lugar(request):
    return TemplateView.as_view(template_name="home.html")(request)

def estado(request):
    return TemplateView.as_view(template_name="home.html")(request)

