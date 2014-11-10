# -*- coding: utf-8 -*-
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from datetime import datetime
from .models import *

# Create your views here.

def home(request):
	sliders = Slider.objects.filter(activo = True)
	titulo = "Home - "
	now = datetime.now()
	todasPublicaciones = Publicacion.objects.filter(
		Q(fecha_inicio__lte=now),
		Q(fecha_fin__gte=now) | Q(fecha_fin__isnull=True), 
		Q(activo = True)).order_by("-categoria")

	publicacionesPermanentes = todasPublicaciones[:4]
	publicaciones = todasPublicaciones[4:8]


	return render(
			request,
			"home.html",
			{
				"sliders": sliders,
				"publicacionesPermanentes" : publicacionesPermanentes,
				"publicaciones" : publicaciones,
				"titulo" : titulo
			}
		)

def directorio(request):
	titulo = "Directorio - "
	return render(
		request,
		"directorio.html",
		{
			"titulo" : titulo,
		}
	)

def historia(request):
	titulo = "Historia - "
	return render(
		request,
		"historia.html",
		{
			"titulo" : titulo,
		}
	)

def licenciaturas_ingenierias(request):
	titulo = "Licenciaturas - Ingenierias - "
	return render(
		request,
		"licenciaturas-ingenierias.html",
		{
			"titulo" : titulo,
		}
	)

def mision_vision(request):
	titulo = "Misión - Visión - "
	return render(
		request,
		"mision-vision.html",
		{
			"titulo" : titulo,
		}
	)

def plano(request):
	titulo = "Plano - "
	return render(
			request,
			"plano.html",
			{
				"titulo" : titulo,
			}
		)

def postgrados(request):
	titulo = "Postgrados - "
	return render(
			request,
			"postgrados.html",
			{
				"titulo" : titulo,
			}
		)

def publicacion(request, ide):
	publicacion = get_object_or_404(Publicacion,activo = True, id=ide)
	titulo = "%s - " % (publicacion.titulo,)
	return render(
		request,
		"publicacion.html",
		{
			"publicacion" : publicacion,
			"titulo" : titulo,
		}
	)

def publicaciones(request):
	titulo = "Publicaciones - "
	now = datetime.now()
	todasPublicaciones = Publicacion.objects.filter(
		Q(fecha_inicio__lte=now) & 
		Q(fecha_fin__gte=now) | Q(fecha_fin__isnull=True), 
		Q(activo = True)).order_by("-categoria")

	publicacionesPermanentes = todasPublicaciones[:4]
	publicaciones = todasPublicaciones[4:8]

	return render(
		request,
		"publicaciones.html",
		{
			"publicacionesPermanentes" : publicacionesPermanentes,
			"publicaciones" : publicaciones,
			"titulo" : titulo
		}
	)