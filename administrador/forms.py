# -*- coding: utf-8 -*-
from django import forms

class BusquedaForm(forms.Form):
	pista = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'¿Qué publicación esta buscando?'}))