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

################################################################################################
@cache_page(60 * cache_time)
def mensaje_director(request):
	titulo = "Mensaje del director - "
	return render(
		request,
		"mensaje-director.html",
		{
			"titulo" : titulo,
		}
	)
@cache_page(60 * cache_time)
def residencias_profesionales(request):
	titulo = "Residencias profesionales - "
	return render(
		request,
		"residencias-profesionales.html",
		{
			"titulo" : titulo,
		}
	)
@cache_page(60 * cache_time)
def cuerpos_academicos(request):
	titulo = "Cuerpos académicos - "
	return render(
		request,
		"cuerpos-academicos.html",
		{
			"titulo" : titulo,
		}
	)

#NORMATIVIDAD
@cache_page(60 * cache_time)
def normatividad_academica(request):
	titulo = "Normatividad académica - "
	return render(
		request,
		"normatividad-academica.html",
		{
			"titulo" : titulo,
		}
	)
@cache_page(60 * cache_time)
def normatividad_lineamientos_academicos(request):
	titulo = "Lineamientos académicos - "
	return render(
		request,
		"normatividad-lineamientos-academicos.html",
		{
			"titulo" : titulo,
		}
	)

@cache_page(60 * cache_time)
def normatividad_manuales_academicos(request):
	titulo = "Manuales académicos - "
	return render(
		request,
		"normatividad-manuales-academicos.html",
		{
			"titulo" : titulo,
		}
	)

@cache_page(60 * cache_time)
def titulacion(request):
	titulo = "Titulación - "
	return render(
		request,
		"titulacion.html",
		{
			"titulo" : titulo,
		}
	)

@cache_page(60 * cache_time)
def tramites(request):
	titulo = "Tramites - "
	return render(
		request,
		"tramites.html",
		{
			"titulo" : titulo,
		}
	)

@cache_page(60 * cache_time)
def documentos_rectores_de_planeacion(request):
	titulo = "Documentos rectores de planeación - "
	return render(
		request,
		"documentos-rectores-de-planeacion.html",
		{
			"titulo" : titulo,
		}
	)

@cache_page(60 * cache_time)
def directorio(request):
	titulo = "Directorio - "
	return render(
		request,
		"directorio.html",
		{
			"titulo" : titulo,
		}
	)

@cache_page(60 * cache_time)
def historia(request):
	titulo = "Historia - "
	return render(
		request,
		"historia.html",
		{
			"titulo" : titulo,
		}
	)

@cache_page(60 * cache_time)
def licenciaturas_ingenierias(request):
	titulo = "Licenciaturas - Ingenierias - "
	return render(
		request,
		"licenciaturas-ingenierias.html",
		{
			"titulo" : titulo,
		}
	)

@cache_page(60 * cache_time)
def mision_vision(request):
	titulo = "Misión - Visión - "
	return render(
		request,
		"mision-vision.html",
		{
			"titulo" : titulo,
		}
	)

@cache_page(60 * cache_time)
def plano(request):
	titulo = "Plano - "
	return render(
			request,
			"plano.html",
			{
				"titulo" : titulo,
			}
		)

@cache_page(60 * cache_time)
def posgrado(request):
	titulo = "Posgrado - "
	return render(
			request,
			"posgrado.html",
			{
				"titulo" : titulo,
			}
		)

@cache_page(60 * cache_time)
def centro_de_informacion(request):
	titulo = "Centro de información - "
	return render(
			request,
			"centro-de-informacion.html",
			{
				"titulo" : titulo,
			}
		)
#############aun no sirve nada
@cache_page(60 * cache_time)
def centro_de_computo(request):
	titulo = "Centro de cómputo - "
	return render(
			request,
			"centro-de-computo.html",
			{
				"titulo" : titulo,
			}
		)

@cache_page(60 * cache_time)
def servicio_social(request):
	titulo = "Servicio social - "
	return render(
			request,
			"servicio-social.html",
			{
				"titulo" : titulo,
			}
		)

@cache_page(60 * cache_time)
def normatividad_planeacion(request):
	titulo = "Normatividad de planeación - "
	return render(
			request,
			"normatividad-planeacion.html",
			{
				"titulo" : titulo,
			}
		)

################################################################################################
def e404(request):
	return render(request,"404.html",{})

def e500(request):
	return render(request,"500.html",{})

################################################################################################	

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
