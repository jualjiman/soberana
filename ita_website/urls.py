# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView
from administrador import views

admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'ita_website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'administrador.views.home', name='home'),
    url(r'^ckeditor/', include('ckeditor.urls')),

    # NUESTRO INSTITUTO
    url(
        r'^nuestro-instituto/mensaje-director/$',
        TemplateView.as_view(template_name="mensaje-director.html"),
        {'titulo': "Mensaje del director"},
        name='mensaje_director'
    ),

    url(
        r'^nuestro-instituto/mision-vision/$',
        TemplateView.as_view(template_name="mision-vision.html"),
        {'titulo': "Misión - Visión"},
        name='mision_vision'
    ),

    url(
        r'^nuestro-instituto/plano/$',
        TemplateView.as_view(template_name="plano.html"),
        {'titulo': "Plano"},
        name='plano'
    ),

    url(
        r'^nuestro-instituto/historia/$',
        TemplateView.as_view(template_name="historia.html"),
        {'titulo': "Historia"},
        name='historia'
    ),

    url(
        r'^nuestro-instituto/directorio/$',
        TemplateView.as_view(template_name="directorio.html"),
        {'titulo': "Directorio"},
        name='directorio'
    ),

    url(
        r'^nuestro-instituto/ubicacion-contacto/$',
        TemplateView.as_view(template_name="ubicacion-contacto.html"),
        {'titulo': "Ubicación y contacto"},
        name='ubicacion_contacto'
    ),

    # PUBLICACIONES
    url(
        r'^publicaciones/$',
        'administrador.views.publicaciones',
        name='publicaciones'
    ),

    url(
        r'^publicaciones/(\d+)/$',
        'administrador.views.publicacion',
        name='publicacion'
    ),

    url(
        r'^eventos/$',
        'administrador.views.eventos',
        name='eventos'
    ),

    # OFERTA EDUCATIVA
    url(
        r'^oferta-educativa/licenciaturas-ingenierias/arquitectura$',
        TemplateView.as_view(template_name="arquitectura.html"),
        {'titulo': "Arquitectura"},
        name='arquitectura'
    ),
    url(
        r'^oferta-educativa/licenciaturas-ingenierias/'
        'ingenieria-en-sistemas-computacionales$',
        TemplateView.as_view(
            template_name="ingenieria-en-sistemas-computacionales.html"
        ),
        {'titulo': "Ingeniería en Sistemas Computacionales"},
        name='ingenieria_en_sistemas_computacionales'
    ),
    url(
        r'^oferta-educativa/licenciaturas-ingenierias/'
        'ingenieria-electromecanica$',
        TemplateView.as_view(template_name="ingenieria-electromecanica.html"),
        {'titulo': "Ingeniería Electromecánica"},
        name='ingenieria_electromecanica'
    ),
    url(
        r'^oferta-educativa/licenciaturas-ingenierias/ingenieria-bioquimica$',
        TemplateView.as_view(template_name="ingenieria-bioquimica.html"),
        {'titulo': "Ingeniería Bioquímica"},
        name='ingenieria_bioquimica'
    ),
    url(
        r'^oferta-educativa/licenciaturas-ingenierias/'
        'ingenieria-en-gestion-empresarial$',
        TemplateView.as_view(
            template_name="ingenieria-en-gestion-empresarial.html"
        ),
        {'titulo': "Ingeniería en Gestión Empresarial"},
        name='ingenieria_en_gestion_empresarial'
    ),
    url(
        r'^oferta-educativa/licenciaturas-ingenierias/'
        'licenciatura-en-administracion$',
        TemplateView.as_view(
            template_name="licenciatura-en-administracion.html"
        ),
        {'titulo': "Licenciatura en Administración"},
        name='licenciatura_en_administracion'
    ),
    url(
        r'^oferta-educativa/licenciaturas-ingenierias/'
        'licenciatura-en-contabilidad$',
        TemplateView.as_view(
            template_name="licenciatura-en-contabilidad.html"
        ),
        {'titulo': "Licenciatura en Contabilidad"},
        name='licenciatura_en_contabilidad'
    ),
    url(
        r'^oferta-educativa/posgrado/$',
        TemplateView.as_view(template_name="posgrado.html"),
        {'titulo': "Posgrado"},
        name='posgrado'
    ),
    url(
        r'^oferta-educativa/cuerpos-academicos/$',
        TemplateView.as_view(template_name="cuerpos-academicos.html"),
        {'titulo': "Cuerpos académicos"},
        name='cuerpos_academicos'
    ),

    #  ASPIRANTES
    url(
        r'^aspirantes/requisitos-ingreso/$',
        TemplateView.as_view(
            template_name="aspirantes-requisitos-de-ingreso.html"
        ),
        {'titulo': "Requisitos de ingreso"},
        name='aspirantes_requisitos_ingreso'
    ),
    url(
        r'^aspirantes/convocatoria/$',
        TemplateView.as_view(
            template_name="aspirantes-convocatoria.html"
        ),
        {'titulo': "Convocatoria aspirantes"},
        name='aspirantes_convocatoria'
    ),
    url(
        r'^aspirantes/resultados/$',
        TemplateView.as_view(template_name="aspirantes-resultados.html"),
        {'titulo': "Aspirantes Resultados"},
        name='aspirantes_resultados'
    ),
    url(
        r'^aspirantes/curso-induccion/$',
        TemplateView.as_view(template_name="aspirantes-curso.html"),
        {'titulo': "Curso de inducción"},
        name='aspirantes_curso_induccion'
    ),

    # ESTUDIANTES
    url(
        r'^estudiantes/servicio-social/$',
        TemplateView.as_view(template_name="servicio-social.html"),
        {'titulo': "Servicio social"},
        name='servicio_social'
    ),
    url(
        r'^estudiantes/creditos-complementarios/$',
        TemplateView.as_view(template_name="creditos-complementarios.html"),
        {'titulo': "Créditos complementarios"},
        name='creditos_complementarios'
    ),
    url(
        r'^estudiantes/residencias-profesionales/$',
        TemplateView.as_view(template_name="residencias-profesionales.html"),
        {'titulo': "Residencias profesionales"},
        name='residencias_profesionales'
    ),
    url(
        r'^estudiantes/titulacion/$',
        TemplateView.as_view(template_name="titulacion.html"),
        {'titulo': "Titulación"},
        name='titulacion'
    ),
    url(
        r'^estudiantes/tramites/$',
        TemplateView.as_view(template_name="tramites.html"),
        {'titulo': "Tramite"},
        name='tramites'
    ),

    # NORMATIVIDAD
    url(
        r'^normatividad/academica/$',
        TemplateView.as_view(template_name="normatividad-academica.html"),
        {'titulo': "Normatividad académica"},
        name='normatividad_academica'
    ),
    url(
        r'^normatividad/planeacion/$',
        TemplateView.as_view(template_name="normatividad-planeacion.html"),
        {'titulo': "Normatividad de planeación"},
        name='normatividad_planeacion'
    ),
    url(
        r'^normatividad/academica/lineamientos-academicos/$',
        TemplateView.as_view(
            template_name="normatividad-lineamientos-academicos.html"
        ),
        {'titulo': "Lineamientos académicos"},
        name='normatividad_lineamientos_academicos'
    ),
    url(
        r'^normatividad/academica/manuales-academicos/$',
        TemplateView.as_view(
            template_name="normatividad-manuales-academicos.html"
        ),
        {'titulo': "Manuales académicos"},
        name='normatividad_manuales_academicos'
    ),

    # SITIOS ITA
    url(
        r'^sitios-ita/documentos-rectores-de-planeacion/$',
        TemplateView.as_view(
            template_name="documentos-rectores-de-planeacion.html"
        ),
        {'titulo': "Documentos rectores de planeación"},
        name='documentos_rectores_de_planeacion'),
    url(
        r'^sitios-ita/modelo-de-equidad-de-genero/$',
        TemplateView.as_view(template_name="modelo-de-equidad-de-genero.html"),
        {'titulo': "Modelo de Equidad de Género"},
        name='modelo_de_equidad_de_genero'
    ),

    #  SERVICIOS
    url(
        r'^servicios/centro-de-informacion/$',
        TemplateView.as_view(template_name="centro-de-informacion.html"),
        {'titulo': "Centro de información"},
        name='centro_de_informacion'
    ),

    # OTROS
    url(r'^busqueda/$', 'administrador.views.busqueda', name='busqueda'),
    url(r'^mas/$', 'administrador.views.mas', name='mas'),

    url(
        r'^static/(?P<path>.*)$',
        'django.views.static.serve',
        {
            'document_root': settings.STATIC_ROOT,
            'show_indexes': True
        }
    ),
    url(
        r'^media/(?P<path>.*)$',
        'django.views.static.serve',
        {
            'document_root': settings.MEDIA_ROOT,
            'show_indexes': True
        }
    ),

    url(r'^api/eventos/$', views.eventos_json, name="eventos_json"),
    url(
        r'^api/publicaciones/$',
        views.publicaciones_json,
        name="publicaciones_json"
    ),
)

handler404 = "administrador.views.e404"
handler500 = "administrador.views.e500"
