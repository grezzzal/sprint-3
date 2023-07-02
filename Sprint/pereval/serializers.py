from .models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = '__all__'


class PerevalImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalImages
        fields = '__all__'

class PerevalAddedSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    coord_id = CoordsSerializer(required=False)
    image = PerevalImagesSerializer(many=True, required=True)

    class Meta:
        model = PerevalAdded
        fields = [
            'beautyTitle', 'title', 'other_titles', 'date_added',
            'connect', 'add_time', 'level_winter', 'level_summer', 'level_autumn',
            'level_spring', 'status',
        ]



