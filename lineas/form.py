from django.forms import ModelForm, TextInput
from django import forms
from geoposition.fields import GeopositionField

from lineas.models import Linea, Posicion, Zona, Calle

class LineaForm(ModelForm):
    class Meta:
        model = Linea
        exclude = ['asociacion']

class MapaForm(ModelForm):
    class Meta:
        model = Posicion
        exclude = ['linea', 'subida', 'bajada']

class ZonaForm(ModelForm):
    class Meta:
        model = Zona
        fields = '__all__'

class CalleForm(ModelForm):
    class Meta:
        model = Calle
        fields = ['zona', 'nombre']
        #class="typeahead" id="product_search" type="text" placeholder="States of USA"
        widgets = {
            'nombre':TextInput(attrs={'type':'text', 'id':'product_search', 'class':'typeahead','placeholder':'Nombre de Calle'})
        }
