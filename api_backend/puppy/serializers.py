from rest_framework import serializers

from puppy.models import Puppy, User


class PuppySerializer(serializers.ModelSerializer):
    class Meta:
        model = Puppy
        # fields = ['name', 'age', 'race', 'vaccinated']
        fields = '__all__'
