# -*- coding: utf-8 -*-
import json
import locale
from datetime import datetime

from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail

from .forms import ContactoForm, BusquedaForm
from .models import *

locale.setlocale(locale.LC_ALL, 'es_MX.utf8')

# Create your views here.

cache_time = 2  # minutos


def queryset(now):
    query = Publicacion.objects.filter(
        Q(fecha_inicio__lte=now),
        Q(fecha_fin__gte=now) | Q(fecha_fin__isnull=True),
        Q(activo=True)).order_by("-fecha", "-categoria", "-pk")
    return query


def home(request):
    sliders = Slider.objects.filter(
        activo=True
    )

    eventos = Evento.objects.filter(
        activo=True,
        fechaHora__gte=datetime.now()
    ).order_by("fechaHora")[:3]

    titulo = "Home"

    query = queryset(datetime.now())
    todas_publicaciones = query

    publicaciones_permanentes = todas_publicaciones[:3]
    publicaciones = todas_publicaciones[3:6]

    if len(eventos) == 0:
        publicaciones = todas_publicaciones[3:7]

    searchform = BusquedaForm()
    return render(
        request,
        "home.html",
        {
            "sliders": sliders,
            "eventos": eventos,
            "publicacionesPermanentes": publicaciones_permanentes,
            "publicaciones": publicaciones,
            "titulo": titulo,
            "searchform": searchform
        }
    )


@cache_page(60 * cache_time)
def publicacion(request, ide):

    query = Publicacion.objects.filter(
        activo=True
    ).order_by(
        "-fecha", 
        "-categoria", 
        "-pk"
    )

    publicacion = get_object_or_404(query, id=ide)

    if(publicacion is not None):
        enlaces = EnlacePublicacion.objects.filter(
            publicacion=publicacion.id)
        videos = VideoPublicacion.objects.filter(
            publicacion=publicacion.id)
        archivos = ArchivoPublicacion.objects.filter(
            publicacion=publicacion.id)

    otras_publicaciones = query.exclude(pk=ide)[:4]

    titulo = "%s" % (publicacion.titulo,)
    description = publicacion.resumen
    searchform = BusquedaForm()
    return render(
        request,
        "publicacion.html",
        {
            "publicacion": publicacion,
            "enlaces": enlaces,
            "videos": videos,
            "archivos": archivos,
            "titulo": titulo,
            "otrasPublicaciones": otras_publicaciones,
            "searchform": searchform,
            "description": description,
        }
    )


def publicaciones(request):
    titulo = "Publicaciones"
    now = datetime.now()

    todas_publicaciones = Publicacion.objects.filter(
        activo=True
    ).order_by(
        "-fecha", 
        "-categoria", 
        "-pk"
    )
    
    publicaciones_permanentes = todas_publicaciones[:4]
    publicaciones = todas_publicaciones[4:8]

    searchform = BusquedaForm()

    return render(
        request,
        "publicaciones.html",
        {
            "publicacionesPermanentes": publicaciones_permanentes,
            "publicaciones": publicaciones,
            "titulo": titulo,
            "searchform": searchform
        }
    )


def publicaciones_json(request):
    publicaciones = queryset(datetime.now())
    result = []
    for i in publicaciones:
        data = {}
        data['titulo'] = i.titulo
        data['resumen'] = i.resumen
        data['fecha'] = str(i.fecha)
        data['imagen'] = ""
        if i.imagen:
            data['imagen'] = i.imagen.url
        result.append(data)

    return HttpResponse(
        json.dumps(result),
        content_type="application/json"
    )


def eventos(request):
    titulo = "Eventos"

    eventos = Evento.objects.filter(
        activo=True,
        fechaHora__gte=datetime.now()
    ).order_by("fechaHora")

    return render(
        request,
        "eventos.html",
        {
            "titulo": titulo,
            "eventos": eventos
        }
    )


def eventos_json(request):

    eventos = Evento.objects.filter(
        activo=True,
        fechaHora__gte=datetime.now()
    ).order_by("fechaHora")

    result = []
    format = "%A %d de %B del %Y a las %H:%M"
    for i in eventos:
        data = {}
        data['titulo'] = i.titulo
        data['descripcion'] = i.descripcion
        data['fechaHora'] = i.fechaHora.strftime(format)
        data['fechaHoraFin'] = ""

        if i.fechaHoraFin:
            data['fechaHoraFin'] = i.fechaHoraFin.strftime(format)
        data['textoLink'] = i.textoLink
        data['link'] = i.link
        result.append(data)

    return HttpResponse(
        json.dumps(result),
        content_type="application/json"
    )


def busqueda(request):
    if request.method == 'GET':  # If the form has been submitted...
        # ContactForm BusquedaForm was defined in the previous section
        # FUNCIONA PERFECTAMENTE POR GET O POST
        searchform = BusquedaForm(request.GET)  # A form bound to the POST data
        if searchform.is_valid():  # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            pista = searchform.cleaned_data['pista']
            if pista != u'':
                now = datetime.now()
                publicaciones = Publicacion.objects.filter(
                    Q(fecha_inicio__lte=now),
                    Q(fecha_fin__gte=now) | Q(fecha_fin__isnull=True),
                    Q(activo=True),
                    Q(titulo__icontains=pista) |
                    Q(resumen__icontains=pista) |
                    Q(texto__icontains=pista)
                ).order_by("-fecha", "-categoria", "-pk")

                texto_busqueda = 'Resultados para "' + pista + '"'
                searchform = BusquedaForm()

                return render(
                    request,
                    'busqueda.html',
                    {
                        "publicaciones": publicaciones,
                        "textoBusqueda": texto_busqueda,
                        "searchform": searchform,
                        "titulo": texto_busqueda
                    }
                )

            else:
                return HttpResponseRedirect("/")
        else:
            return HttpResponseRedirect("/")
    else:
        return HttpResponseRedirect("/")


def contacto(request):
    if request.is_ajax():
        nombre = request.POST['name']
        email = request.POST['email']
        mensaje = request.POST['message']

        dfrom = nombre + " <" + email + ">"
        mensaje = dfrom + "\n\n" + mensaje

        send_mail(
            'Mensaje desde Pagina web ITA',
            mensaje,
            "ITA Quejas y sujerencias <quejas_y_sugerencias@it-acapulco.edu.mx>",
            ['jualjiman@gmail.com', ],
            fail_silently=False
        )

        send_mail(
            'Mensaje desde Pagina web ITA',
            mensaje,
            "ITA Quejas y sujerencias <quejas_y_sugerencias@it-acapulco.edu.mx>",
            ['jualjiman@gmail.com', ],
            fail_silently=False
        )

        return HttpResponse('Ok')
    else:
        form = ContactoForm()
        return render(
            request,
            "ubicacion-contacto.html",
            {
                "form": form,
                'titulo': "Ubicación y contacto",
            })


@csrf_exempt
def mas(request):
    if request.is_ajax():
        pagina = int(request.POST['num'])
        elems_por_pagina = 4
        pagina *= elems_por_pagina

        query = Publicacion.objects.filter(
            activo=True
        ).order_by(
            "-fecha", 
            "-categoria", 
            "-pk"
        )
         
        mas_publicaciones = query[pagina:(pagina + elems_por_pagina)]

        return render(
            request,
            "mas.html",
            {"masPublicaciones": mas_publicaciones}
        )
    else:
        return HttpResponseRedirect("/")


def e404(request):
    return render(
        request,
        "404.html",
        {}
    )


def e500(request):
    return render(
        request,
        "500.html",
        {}
    )
