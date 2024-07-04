from django import forms

class MaestriasForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    modalidad = forms.CharField(max_length=50)