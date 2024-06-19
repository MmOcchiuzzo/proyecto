from django import forms

from barbie_api.models import Barbie, User
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime

# def validate_number(value):
#     if not isinstance(value, int):
#         raise ValidationError("El numero debe ser un número entero.")
#     if value > -1:
#         raise ValidationError("El año de aparición debe tener exactamente 4 dígitos.")

class BarbieForm(forms.ModelForm):

    # name = forms.CharField(label=False,
    #                        widget=forms.TextInput(attrs={'placeholder': 'Barbie name'}))
    # number = forms.IntegerField(label=False,
    #                             widget=forms.TextInput(attrs={'placeholder': 'Barbie number'}),
    #                             validators=[validate_number])
    # collection = forms.CharField(label=False,
    #                              widget=forms.TextInput(attrs={'placeholder': 'Barbie collection'}))
    class Meta:
        model = Barbie
        fields = [
            'name',
            'number',
            'collection',
            'sold',
        ]

class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = [
            'name',
            'barbies',
        ]