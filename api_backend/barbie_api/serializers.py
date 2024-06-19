from rest_framework import serializers

from barbie_api.models import Barbie, User


class BarbieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barbie
        # fields = ['name', 'number', 'collection', 'sold']
        fields = '__all__'