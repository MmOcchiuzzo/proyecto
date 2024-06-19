from django import forms
from puppy.models import Puppy, User

class PuppyForm(forms.ModelForm):
    class Meta:
        model = Puppy
        fields = [
            'name',
            'age',
            'breed',
            'vaccinated',
        ]

class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = [
            'name',
            'puppies',
        ]