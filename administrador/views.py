# -*- coding: utf-8 -*-
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from datetime import datetime
from .models import *
from .forms import *

from django.views.decorators.cache import cache_page

# Create your views here.

cache_time = 2 #minutos

@cache_page(60 * cache_time)
def home(request):
	sliders = Slider.objects.filter(activo = True)
	titulo = "Home - "
	now = datetime.now()
	todasPublicaciones = Publicacion.objects.filter(
		Q(fecha_inicio__lte=now),
		Q(fecha_fin__gte=now) | Q(fecha_fin__isnull=True), 
		Q(activo = True)).order_by("-fecha","-categoria","-pk")

	publicacionesPermanentes = todasPublicaciones[:4]
	publicaciones = todasPublicaciones[4:8]

	searchform = BusquedaForm()
	return render(
			request,
			"home.html",
			{
				"sliders": sliders,
				"publicacionesPermanentes" : publicacionesPermanentes,
				"publicaciones" : publicaciones,
				"titulo" : titulo,
				"searchform" : searchform
			}
		)

@cache_page(60 * cache_time)
def publicacion(request, ide):

	now = datetime.now()
	queryset = Publicacion.objects.filter(
		Q(fecha_inicio__lte=now),
		Q(fecha_fin__gte=now) | Q(fecha_fin__isnull=True), 
		Q(activo = True))

	publicacion = get_object_or_404(queryset, id=ide)

	otrasPublicaciones = Publicacion.objects.filter(
		Q(fecha_inicio__lte=now), 
		Q(fecha_fin__gte=now) | Q(fecha_fin__isnull=True), 
		Q(activo = True)).exclude(pk=ide).order_by("-fecha","-categoria","-pk")[:4]

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

@cache_page(60 * cache_time)
def publicaciones(request):
	titulo = "Publicaciones - "
	now = datetime.now()
	todasPublicaciones = Publicacion.objects.filter(
		Q(fecha_inicio__lte=now), 
		Q(fecha_fin__gte=now) | Q(fecha_fin__isnull=True), 
		Q(activo = True)).order_by("-fecha","-categoria","-pk")

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

@cache_page(60 * cache_time)
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
					).order_by("-fecha","-categoria","-pk")

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

def residencias_profesionales(request):
	titulo = "Residencias profesionales - "
	return render(
		request,
		"residencias-profesionales.html",
		{
			"titulo" : titulo,
		}
	)

def titulacion(request):
	titulo = "Titulación - "
	return render(
		request,
		"titulacion.html",
		{
			"titulo" : titulo,
		}
	)

def formatos(request):
	titulo = "Formatos - "
	return render(
		request,
		"formatos.html",
		{
			"titulo" : titulo,
		}
	)

def documentos_rectores_de_planeacion(request):
	titulo = "Documentos rectores de planeación - "
	return render(
		request,
		"documentos-rectores-de-planeacion.html",
		{
			"titulo" : titulo,
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
