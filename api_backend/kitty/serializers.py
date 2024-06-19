from rest_framework import serializers

from kitty.models import Kitty, User


class KittySerializer(serializers.ModelSerializer):
    class Meta:
        model = Kitty
        # fields = ['name', 'breed', 'fur', 'color']
        fields = '__all__'