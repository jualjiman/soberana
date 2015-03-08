# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.

categorias = (
	(1, u'Importante'),
	(0, u'Normal'),
)

class Slider(models.Model):
	imagen = ImageField(upload_to = "sliders")
	titulo = models.CharField(max_length=60,blank=True, help_text='Titulo que aparecera en el recuadro rojo')
	link = models.CharField(max_length=300, blank=True, help_text="Link al que enviara el slide")
	orden = models.IntegerField(default=100, help_text="Numeros mayores van primero")
	activo = models.BooleanField(default=True, help_text="Debera ser mostrado?")
	
	def __str__(self):
		return self.titulo

class Publicacion(models.Model):
	class Meta:
		verbose_name_plural = "Publicaciones"
	activo = models.BooleanField(default=False, help_text="Debera ser mostrado?")
	imagen = ImageField(blank=True, upload_to = "publicaciones")
	titulo = models.CharField(max_length=60, help_text='Titulo de la publicacion')
	resumen = models.CharField(max_length=150, help_text='Reseña de la publicacion que sera mostrada (150 caracteres)')

	texto = RichTextField()
	
	fecha = models.DateField(default=datetime.now(),help_text='Fecha que sera mostrada en la publicación')
	fecha_inicio = models.DateTimeField(default=datetime.now(), help_text='Fecha y hora de inicio de la publicación')
	fecha_fin = models.DateTimeField(blank=True,null=True, help_text='Fecha y hora en que dejara de ser mostrada la publicación. Si se deja en blanco sera permanente')
	
	categoria = models.IntegerField(choices=categorias, help_text='Define la prioridad de la publicación')

	editer = models.ForeignKey(User, related_name='ModificoPublicacion', null=True, blank=True)
	creator = models.ForeignKey(User, related_name='CreadorPublicacion', null=True, blank=True)
	
	def __str__(self):
		return self.titulo

class EnlacePublicacion(models.Model):
	class Meta:
		verbose_name_plural = "Enlaces de publicación"
	descripcionLink = models.CharField(max_length=60, help_text="Texto descriptivo del link.")
	link = models.URLField(help_text='Link asociado con la publicacion')
	publicacion = models.ForeignKey(Publicacion)


class VideoPublicacion(models.Model):
	class Meta:
		verbose_name_plural = "Videos de publicacion"
	descripcionVideoYoutube = models.CharField(max_length=60, help_text="Texto descriptivo del video de youtube.")
	claveYoutube = models.CharField(max_length=20, help_text='Clave de video de youtube asociado con la publicacion')
	publicacion = models.ForeignKey(Publicacion)

class ArchivoPublicacion(models.Model):
	class Meta:
		verbose_name_plural = "Archivo de publicación"
	descripcionArchivo = models.CharField(max_length=60, help_text="Texto descriptivo del archivo.")
	archivo = models.FileField(upload_to = "pdfpublicacion", help_text='Archivo asociado con la publicacion')
	publicacion = models.ForeignKey(Publicacion)

class Evento(models.Model):
	titulo = models.CharField(max_length=100, help_text="Titulo del evento")
	descripcion = models.TextField(blank=True, help_text="Descripcion del evento")
	fechaHora = models.DateTimeField(default=datetime.now(), help_text="Fecha y hora del evento")
	fechaHoraFin = models.DateTimeField(blank=True,null=True, help_text="Fecha y hora de fin del evento")
	textoLink = models.CharField(max_length=300, blank=True, help_text="Texto del link")
	link = models.CharField(max_length=300, blank=True, help_text="Link al que enviara el evento")
	activo = models.BooleanField(default=False, help_text="Debera ser mostrado?")

	def __str__(self):
		return self.titulo
