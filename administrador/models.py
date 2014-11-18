 # -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField
from datetime import datetime

# Create your models here.

categorias = (
	(1, u'Importante'),
	(0, u'Normal'),
)

class Slider(models.Model):
	imagen = ImageField(upload_to = "sliders")
	titulo = models.CharField(max_length=60,blank=True, help_text='Titulo que aparecera en el recuadro rojo')
	orden = models.IntegerField(default=100, help_text="Numeros mayores van primero")
	activo = models.BooleanField(default=True, help_text="Debera ser mostrado?")

	def __str__(self):
		return self.titulo

class Publicacion(models.Model):
	activo = models.BooleanField(default=False, help_text="Debera ser mostrado?")
	imagen = ImageField(upload_to = "publicaciones")
	titulo = models.CharField(max_length=60, help_text='Titulo de la publicacion')
	resumen = models.CharField(max_length=150, help_text='Reseña de la publicacion que sera mostrada (150 caracteres)')
	texto = models.TextField(help_text='Texto correspondiente a la publicacion')
	descripcionLink = models.CharField(max_length=60, blank=True, help_text="Texto descriptivo del link.")
	link = models.URLField(blank=True, help_text='Link asociado con la publicacion')
	descripcionVideoYoutube = models.CharField(max_length=60, blank=True, help_text="Texto descriptivo del video de youtube.")
	claveYoutube = models.CharField(max_length=20, blank=True, help_text='Clave de video de youtube asociado con la publicacion')
	descripcionPdf = models.CharField(max_length=60, blank=True, help_text="Texto descriptivo del PDF.")
	pdf = models.FileField(upload_to = "pdfpublicacion", blank=True, help_text='Archivo pdf asociado con la publicacion')
	fecha = models.DateField(default=datetime.now(),help_text='Fecha a partir de la cual sera mostrada la publicacion')
	fecha_inicio = models.DateTimeField(default=datetime.now(), help_text='Fecha y hora de inicio de la publicacion')
	fecha_fin = models.DateTimeField(blank=True,null=True, help_text='Fecha y hora en que dejara de ser mostrada la publicacion. Si se deja en blanco sera permanente')
	categoria = models.IntegerField(choices=categorias, help_text='Define la prioridad de la publicacion')

	editer = models.ForeignKey(User, related_name='ModificoPublicacion', null=True, blank=True)
	creator = models.ForeignKey(User, related_name='CreadorPublicacion', null=True, blank=True)
	
	def __str__(self):
		return self.titulo
