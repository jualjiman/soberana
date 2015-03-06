from django.contrib import admin
from .models import *
from sorl.thumbnail.shortcuts import get_thumbnail
from django.contrib.auth.models import User

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

# Register your models here.

#UserAdmin.list_display = ('username', 'email', 'first_name', 'last_name','get_group_permissions')

class CustomUserAdmin(UserAdmin):
	list_display = ('username', 'email', 'first_name', 'last_name', 'grupos')

	def save_model(self, request, obj, form, change):
		obj.is_staff = True
		obj.save()

	## Static overriding 
	fieldsets = (
	    (None, {'fields': ('username', 'password')}),
	    (('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
	    (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups')}),
	    #(('Important dates'), {'fields': ('last_login', 'date_joined')}),
	)

	def get_form(self, request, obj=None, **kwargs):
	    self.exclude = ("user_permissions",)
	    ## Dynamically overriding
	    self.fieldsets[2][1]["fields"] = ('groups',)
	    
	    form = super(CustomUserAdmin,self).get_form(request, obj, **kwargs)
	    return form
	def grupos(self,model_instance):
		grupos = model_instance.groups.all()
		string_grupos = ""
		
		for nombre in grupos:
			string_grupos += str(nombre) + " "

		return string_grupos

class EnlaceInline(admin.StackedInline):
	model = EnlacePublicacion
	extra = 0

class VideoInline(admin.StackedInline):
	model = VideoPublicacion
	extra = 0

class ArchivoInline(admin.StackedInline):
	model = ArchivoPublicacion
	extra = 0

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
	list_display = ('img_slider','titulo','link','activo',)
	search_fields = ('titulo',)

	def img_slider(self,model_instance):
		return "<img src='%s' />" % (get_thumbnail(model_instance.imagen,'250x100',crop='center').url,)

	img_slider.allow_tags = True

@admin.register(Publicacion)
class PublicacionAdmin(admin.ModelAdmin):

	list_display = ('img_publicacion','fecha','titulo','fecha_inicio','fecha_fin','categoria','activo','creador','ultima_modificacion')
	search_fields = ('titulo','texto','resumen',)
	inlines = [EnlaceInline, VideoInline, ArchivoInline, ]

	def img_publicacion(self,model_instance):
		return "<img src='%s' />" % (get_thumbnail(model_instance.imagen,'100x66',crop='center').url,)

	def creador(self,model_instance):
		return model_instance.creator

	def ultima_modificacion(self,model_instance):
		return model_instance.editer
	
	img_publicacion.allow_tags = True		

	def save_model(self, request, publication, form, change):
		if change:
			publication.editer = request.user
		else:
			publication.creator = request.user
		
		publication.save()

	def get_form(self, request, obj=None, **kwargs):
		if request.user.groups.filter(name='Capturista').exists():
			self.exclude = ['activo','creator','editer']
		else:
			self.exclude = ['creator','editer']

		return super(PublicacionAdmin, self).get_form(request, obj, **kwargs)

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
	list_display = ('titulo','fechaHora','activo')
	search_fields = ('titulo','descripcion')

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.unregister(Group)
