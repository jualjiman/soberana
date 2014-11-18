from django.contrib import admin
from .models import *
from sorl.thumbnail.shortcuts import get_thumbnail

# Register your models here.

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
	list_display = ('img_slider','titulo','activo',)
	search_fields = ('titulo',)

	def img_slider(self,model_instance):
		return "<img src='%s' />" % (get_thumbnail(model_instance.imagen,'250x100',crop='center').url,)

	img_slider.allow_tags = True

@admin.register(Publicacion)
class PublicacionAdmin(admin.ModelAdmin):

	list_display = ('img_publicacion','fecha','titulo','fecha_inicio','fecha_fin','categoria','activo')
	search_fields = ('titulo','descripcion',)

	def img_publicacion(self,model_instance):
		return "<img src='%s' />" % (get_thumbnail(model_instance.imagen,'150x100',crop='center').url,)
	
	img_publicacion.allow_tags = True		

	def save_model(self, request, publication, form, change):
              publication.creator = request.user
              publication.save()

    def get_form(self, request, obj=None, **kwargs):
		if request.user.groups.filter(name='Capturista').exists():
			self.exclude = ['activo']
		else:
			self.exclude = []

		return super(PublicacionAdmin, self).get_form(request, obj, **kwargs)