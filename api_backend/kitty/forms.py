from django import forms
from kitty.models import Kitty, User

class KittyForm(forms.ModelForm):
    class Meta:
        model = Kitty
        fields = [
            'name',
            'breed',
            'fur',
            'color',
        ]

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'name',
            'kitties',
        ]
