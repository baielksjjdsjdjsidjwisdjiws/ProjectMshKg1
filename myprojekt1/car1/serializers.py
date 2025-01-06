from rest_framework import serializers
from .models import *


class CarMakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarMake
        fields = '__all__'


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'



class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'car_name', 'description', 'price',
                  'image', 'volum', 'year', 'color',
                  'CarMake_name', 'car_model_name', 'created_date']

