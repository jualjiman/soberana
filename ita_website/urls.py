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
    url(r'^directorio/$', 'administrador.views.directorio', name='directorio'),
    url(r'^publicacion/(\d+)/$', 'administrador.views.publicacion', name='publicacion'),
    url(r'^publicaciones/$', 'administrador.views.publicaciones', name='publicaciones'),
    url(r'^busqueda/$', 'administrador.views.busqueda', name='busqueda'),

    url(r'^documentos-rectores-de-planeacion/$', 'administrador.views.documentos_rectores_de_planeacion', name='documentos_rectores_de-planeacion'),
    url(r'^residencias-profesionales/$', 'administrador.views.residencias_profesionales', name='residencias_profesionales'),
    url(r'^historia/$', 'administrador.views.historia', name='historia'),
    url(r'^formatos/$', 'administrador.views.formatos', name='formatos'),
    url(r'^titulacion/$', 'administrador.views.titulacion', name='titulacion'),
    url(r'^licenciaturas-ingenierias/$', 'administrador.views.licenciaturas_ingenierias', name='licenciaturas_ingenierias'),
    url(r'^mision-vision/$', 'administrador.views.mision_vision', name='mision_vision'),
    url(r'^plano/$', 'administrador.views.plano', name='plano'),
    url(r'^postgrados/$', 'administrador.views.postgrados', name='postgrados'),

    url(r'^mas/$', 'administrador.views.mas', name='mas'),

    #url(r'^contacto/$', 'administrador.views.contacto', name='contacto'),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes':True}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),

    url(r'^e404/$', 'administrador.views.e404', name='e404'),
)

handler404 = "administrador.views.e404"
handler500 = "administrador.views.e500"
