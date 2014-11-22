from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ita_website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'administrador.views.home', name='home'),
    
    #PUBLICACIONES
    url(r'^publicaciones/(\d+)/$', 'administrador.views.publicacion', name='publicacion'),
    url(r'^publicaciones/$', 'administrador.views.publicaciones', name='publicaciones'),
    
    #ESTUDIANTES
    url(r'^estudiantes/residencias-profesionales/$', 'administrador.views.residencias_profesionales', name='residencias_profesionales'),
    url(r'^estudiantes/titulacion/$', 'administrador.views.titulacion', name='titulacion'),
    url(r'^estudiantes/formatos/$', 'administrador.views.formatos', name='formatos'),
    
    #OFERTA EDUCATIVA
    url(r'^oferta-educativa/licenciaturas-ingenierias/$', 'administrador.views.licenciaturas_ingenierias', name='licenciaturas_ingenierias'),
    url(r'^oferta-educativa/posgrado/$', 'administrador.views.posgrado', name='posgrado'),
    url(r'^oferta-educativa/cuerpos-academicos/$', 'administrador.views.cuerpos_academicos', name='cuerpos_academicos'),
    
    #NUESTRO INSTITUTO
    url(r'^nuestro-instituto/mision-vision/$', 'administrador.views.mision_vision', name='mision_vision'),
    url(r'^nuestro-instituto/plano/$', 'administrador.views.plano', name='plano'),
    url(r'^nuestro-instituto/historia/$', 'administrador.views.historia', name='historia'),
    url(r'^nuestro-instituto/directorio/$', 'administrador.views.directorio', name='directorio'),
    
    #SITIOS ITA
    url(r'^sitios-ita/documentos-rectores-de-planeacion/$', 'administrador.views.documentos_rectores_de_planeacion', name='documentos_rectores_de-planeacion'),
    
    #NORMATIVIDAD
    url(r'^normatividad/academica/$', 'administrador.views.normatividad_academica', name='normatividad_academica'),
    url(r'^normatividad/academica/lineamientos-academicos/$', 'administrador.views.normatividad_lineamientos_academicos', name='normatividad_lineamientos_academicos'),
    url(r'^normatividad/academica/manuales-academicos/$', 'administrador.views.normatividad_manuales_academicos', name='normatividad_manuales_academicos'),

    # #CAPTURISTA ADMIN
    # url(r'^capturista/admin$', 'administrador.views.capturista_admin', name='capturista_admin'),
    # url(r'^capturista/admin/all$', 'administrador.views.capturista_admin_lista', name='capturista_admin_lista'),
    # url(r'^capturista/admin/$', 'administrador.views.capturista_admin_lista', name='capturista_admin_lista'),

    #OTROS
    url(r'^busqueda/$', 'administrador.views.busqueda', name='busqueda'),
    url(r'^mas/$', 'administrador.views.mas', name='mas'),

    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes':True}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),

    url(r'^e404/$', 'administrador.views.e404', name='e404'),
)

handler404 = "administrador.views.e404"
handler500 = "administrador.views.e500"
