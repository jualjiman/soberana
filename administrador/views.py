# -*- coding: utf-8 -*-
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from datetime import datetime
from .models import *
from .forms import *

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

def publicacion(request, ide):
	publicacion = get_object_or_404(Publicacion,activo = True, id=ide)

	now = datetime.now()
	otrasPublicaciones = Publicacion.objects.filter(
		Q(fecha_inicio__lte=now), 
		Q(fecha_fin__gte=now) | Q(fecha_fin__isnull=True), 
		Q(activo = True)).exclude(pk=ide).order_by("-categoria")[:4]

	titulo = "%s - " % (publicacion.titulo,)
	searchform = BusquedaForm()
	return render(
		request,
		"publicacion.html",
		{
			"publicacion" : publicacion,
			"titulo" : titulo,
			"otrasPublicaciones" : otrasPublicaciones,
			"searchform" : searchform
		}
	)

def publicaciones(request):
	titulo = "Publicaciones - "
	now = datetime.now()
	todasPublicaciones = Publicacion.objects.filter(
		Q(fecha_inicio__lte=now), 
		Q(fecha_fin__gte=now) | Q(fecha_fin__isnull=True), 
		Q(activo = True)).order_by("-categoria")

	publicacionesPermanentes = todasPublicaciones[:4]
	publicaciones = todasPublicaciones[4:8]

	searchform = BusquedaForm()

	return render(
		request,
		"publicaciones.html",
		{
			"publicacionesPermanentes" : publicacionesPermanentes,
			"publicaciones" : publicaciones,
			"titulo" : titulo,
			"searchform" : searchform
		}
	)

def busqueda(request):
	if request.method == 'GET': # If the form has been submitted...
        # ContactForm BusquedaForm was defined in the previous section
        #FUNCIONA PERFECTAMENTE POR GET O POST
		searchform = BusquedaForm(request.GET) # A form bound to the POST data
		if searchform.is_valid(): # All validation rules pass
	        # Process the data in form.cleaned_data
	        # ...
			pista = searchform.cleaned_data['pista']
			if pista != u'':
				now = datetime.now()
				publicaciones = Publicacion.objects.filter(
					Q(fecha_inicio__lte=now), 
					Q(fecha_fin__gte=now) | Q(fecha_fin__isnull=True), 
					Q(activo = True),
					Q(titulo__icontains= pista) | Q(resumen__icontains=pista) | Q(texto__icontains=pista)
					).order_by("-categoria")

				textoBusqueda = 'Resultados para "' + pista + '"'
				searchform = BusquedaForm()

				return render(request, 'busqueda.html', {
					"publicaciones": publicaciones,
					"textoBusqueda":textoBusqueda,
					"searchform" : searchform
					})
			else:
				return HttpResponseRedirect("/")
		else:
				return HttpResponseRedirect("/")
	else:
		return HttpResponseRedirect("/")

################################################################################################

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