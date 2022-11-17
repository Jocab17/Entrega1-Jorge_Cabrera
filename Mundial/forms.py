from django import forms

class FormRegistrarSeleccion(forms.Form):

    pais = forms.CharField(max_length=40)
    continente = forms.CharField(max_length=40)

class FormRegistrarJugador(forms.Form):

    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    pais = forms.CharField(max_length=40)

class FormRegistrarEstadio(forms.Form):

    nombre = forms.CharField(max_length=40)
    capacidad = forms.IntegerField()