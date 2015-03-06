# -*- coding: utf-8 -*-
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from datetime import datetime
from .models import *
from .forms import *

from django.views.decorators.cache import cache_page

# Create your views here.

cache_time = 2 #minutos

def queryset(now):
	query = Publicacion.objects.filter(
		Q(fecha_inicio__lte=now),
		Q(fecha_fin__gte=now) | Q(fecha_fin__isnull=True), 
		Q(activo = True)).order_by("-fecha","-categoria","-pk")
	return query

def home(request):
	sliders = Slider.objects.filter(activo = True)
	eventos = Evento.objects.filter(activo = True).order_by("-fechaHora")[:4]

	titulo = "Home - "

	query = queryset(datetime.now())
	todasPublicaciones = query

	publicacionesPermanentes = todasPublicaciones[:3]
	publicaciones = todasPublicaciones[3:7]

	searchform = BusquedaForm()
	return render(
			request,
			"home.html",
			{
				"sliders": sliders,
				"eventos": eventos,
				"publicacionesPermanentes" : publicacionesPermanentes,
				"publicaciones" : publicaciones,
				"titulo" : titulo,
				"searchform" : searchform
			}
		)

@cache_page(60 * cache_time)
def publicacion(request, ide):

	query = queryset(datetime.now())

	publicacion = get_object_or_404(query, id=ide)

	if(publicacion != None):
		enlaces = EnlacePublicacion.objects.filter(publicacion = publicacion.id)
		videos = VideoPublicacion.objects.filter(publicacion = publicacion.id)
		archivos = ArchivoPublicacion.objects.filter(publicacion = publicacion.id)

	otrasPublicaciones = query.exclude(pk=ide)[:4]

	titulo = "%s - " % (publicacion.titulo,)
	description = publicacion.resumen
	searchform = BusquedaForm()
	return render(
		request,
		"publicacion.html",
		{
			"publicacion" : publicacion,
			"enlaces" : enlaces,
			"videos" : videos,
			"archivos" : archivos,
			"titulo" : titulo,
			"otrasPublicaciones" : otrasPublicaciones,
			"searchform" : searchform,
			"description" : description,
		}
	)

def publicaciones(request):
	titulo = "Publicaciones - "
	query = queryset(datetime.now())
	todasPublicaciones = query

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

@csrf_exempt
def mas(request):
	if request.is_ajax():
	    pagina = int(request.POST['num'])
	    elemsPorPagina = 4
	    pagina *= elemsPorPagina

	    query = queryset(datetime.now())
	    masPublicaciones = query[pagina:(pagina+elemsPorPagina)]

	    return render(request,"mas.html",{"masPublicaciones": masPublicaciones})
	else:
		return HttpResponseRedirect("/")

def e404(request):
	return render(request,"404.html",{})

def e500(request):
	return render(request,"500.html",{})
