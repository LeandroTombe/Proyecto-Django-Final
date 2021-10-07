from aplicacion.models import Pregunta, participante
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

#mis vistas
from .models import *
from .admin import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username','first_name','last_name', 'email', 'password1', 'password2']



class CustomerForm(ModelForm):
	class Meta:
		model = participante
		fields = '__all__'
		exclude = ['user', 'puntaje_total']

class pregunta(ModelForm):
	class Meta:
		model = Pregunta
		fields = '__all__'


class respuesta(ModelForm):
	class Meta:
		model = ElegirRespuesta
		fields = '__all__'




User = get_user_model()

class ElegirInlineFormset(forms.BaseInlineFormSet):
	def clean(self):
		super(ElegirInlineFormset, self).clean()

		respuesta_correcta = 0
		for formulario in self.forms:
			if not formulario.is_valid():
				return

			if formulario.cleaned_data and formulario.cleaned_data.get('correcta') is True:
				respuesta_correcta += 1

		try:
			assert respuesta_correcta == 1
		except AssertionError:
			raise forms.ValidationError('Exactamente una sola respuesta es permitida')