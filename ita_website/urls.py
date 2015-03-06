# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ita_website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'administrador.views.home', name='home'),
    url(r'^ckeditor/', include('ckeditor.urls')),
    
    #PUBLICACIONES
    url(r'^publicaciones/(\d+)/$', 'administrador.views.publicacion', name='publicacion'),
    url(r'^publicaciones/$', 'administrador.views.publicaciones', name='publicaciones'),
    
    #ESTUDIANTES
    url(r'^estudiantes/residencias-profesionales/$', TemplateView.as_view(template_name="residencias-profesionales.html"), { 'titulo' : "Residencias profesionales" }, name='residencias_profesionales'),
    url(r'^estudiantes/titulacion/$', TemplateView.as_view(template_name="titulacion.html"), { 'titulo' : "Titulación" }, name='titulacion'),
    url(r'^estudiantes/tramites/$', TemplateView.as_view(template_name="tramites.html"), { 'titulo' : "Tramite" }, name='tramites'),
    url(r'^estudiantes/servicio-social/$', TemplateView.as_view(template_name="servicio-social.html"), { 'titulo' : "Servicio social" }, name='servicio_social'),

    
    #OFERTA EDUCATIVA
    url(r'^oferta-educativa/licenciaturas-ingenierias/$', TemplateView.as_view(template_name="licenciaturas-ingenierias.html"), { 'titulo' : "Licenciaturas - Ingenierias" }, name='licenciaturas_ingenierias'),
    url(r'^oferta-educativa/posgrado/$', TemplateView.as_view(template_name="posgrado.html"), { 'titulo' : "Posgrado" }, name='posgrado'),
    url(r'^oferta-educativa/cuerpos-academicos/$', TemplateView.as_view(template_name="cuerpos-academicos.html"), { 'titulo' : "Cuerpos académicos" }, name='cuerpos_academicos'),
    
    #NUESTRO INSTITUTO
    url(r'^nuestro-instituto/mision-vision/$', TemplateView.as_view(template_name="mision-vision.html"), { 'titulo' : "Misión - Visión" }, name='mision_vision'),
    url(r'^nuestro-instituto/plano/$', TemplateView.as_view(template_name="plano.html"), { 'titulo' : "Plano" }, name='plano'),
    url(r'^nuestro-instituto/historia/$', TemplateView.as_view(template_name="historia.html"), { 'titulo' : "Historia" }, name='historia'),
    url(r'^nuestro-instituto/directorio/$', TemplateView.as_view(template_name="directorio.html"), { 'titulo' : "Directorio" }, name='directorio'),
    url(r'^nuestro-instituto/mensaje-director/$', TemplateView.as_view(template_name="mensaje-director.html"), { 'titulo' : "Mensaje del director" }, name='mensaje_director'),

    url(r'^nuestro-instituto/ubicacion-contacto/$', TemplateView.as_view(template_name="ubicacion-contacto.html"), { 'titulo' : "Ubicación y contacto" }, name='ubicacion_contacto'),
    
    #SITIOS ITA
    url(r'^sitios-ita/documentos-rectores-de-planeacion/$', TemplateView.as_view(template_name="documentos-rectores-de-planeacion.html"), { 'titulo' : "Documentos rectores de planeación" }, name='documentos_rectores_de-planeacion'),
    
    #NORMATIVIDAD
    url(r'^normatividad/academica/$', TemplateView.as_view(template_name="normatividad-academica.html"), { 'titulo' : "Normatividad académica" }, name='normatividad_academica'),
    url(r'^normatividad/planeacion/$', TemplateView.as_view(template_name="normatividad-planeacion.html"), { 'titulo' : "Normatividad de planeación" }, name='normatividad_planeacion'),
    url(r'^normatividad/academica/lineamientos-academicos/$', TemplateView.as_view(template_name="normatividad-lineamientos-academicos.html"), { 'titulo' : "Lineamientos académicos" }, name='normatividad_lineamientos_academicos'),
    url(r'^normatividad/academica/manuales-academicos/$', TemplateView.as_view(template_name="normatividad-manuales-academicos.html"), { 'titulo' : "Manuales académicos" }, name='normatividad_manuales_academicos'),

    # SERVICIOS
    #url(r'^servicios/actividades-extraescolares/$', 'administrador.views.actividades_extraescolares', name='actividades_extraescolares'),
    #url(r'^servicios/centro-de-computo/$', 'administrador.views.centro_de_computo', name='centro_de_computo'),
    url(r'^servicios/centro-de-informacion/$', TemplateView.as_view(template_name="centro-de-informacion.html"), { 'titulo' : "Centro de información" }, name='centro_de_informacion'),

    # ASPIRANTES
    url(r'^aspirantes/convocatoria/$', TemplateView.as_view(template_name="aspirantes-convocatoria.html"), { 'titulo' : "Convocatoria aspirantes" }, name='aspirantes_convocatoria'),
    url(r'^aspirantes/requisitos-ingreso/$', TemplateView.as_view(template_name="aspirantes-requisitos-de-ingreso.html"), { 'titulo' : "Requisitos de ingreso" }, name='aspirantes_requisitos_ingreso'),
    url(r'^aspirantes/resultados/$', TemplateView.as_view(template_name="aspirantes-resultados.html"), { 'titulo' : "Aspirantes Resultados" }, name='aspirantes_resultados'),
    url(r'^aspirantes/curso-induccion/$', TemplateView.as_view(template_name="aspirantes-curso.html"), { 'titulo' : "Curso de inducción" }, name='aspirantes_cursos'),

    #OTROS
    url(r'^busqueda/$', 'administrador.views.busqueda', name='busqueda'),
    url(r'^mas/$', 'administrador.views.mas', name='mas'),

    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes':True}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
)

handler404 = "administrador.views.e404"#TemplateView.as_view(template_name="404.html")
handler500 = "administrador.views.e500"
