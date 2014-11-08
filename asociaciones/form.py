from django import forms
from django.forms import ModelForm, DateInput, Textarea, TextInput
from django.contrib.auth.models import User

from asociaciones.models import Asociacion

class AsociacionForm(ModelForm):
    class Meta:
        model = Asociacion
        fields = '__all__'
        exclude = ['usuario']