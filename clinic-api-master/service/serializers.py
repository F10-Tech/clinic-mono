from rest_framework import serializers
from .models import *

# Service

class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = '__all__'

class UpdateServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = ['name_EN', 'description_EN', 'name_AR', 'description_AR', 'name_FR', 'description_FR', 'is_active']

class ServiceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['image_light', 'image_dark']

    class Meta:
        model = Service
        fields = ['name_EN', 'description_EN', 'name_AR', 'description_AR', 'name_FR', 'description_FR', 'is_active']

class ServiceImageSerializer(serializers.ModelSerializer):
    
    # image_light = 


    class Meta:
        model = Service
        fields = ['image_light', 'image_dark']
# Subservice

class SubserviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subservice
        fields = '__all__'

class UpdateSubserviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subservice
        fields = ['name_EN', 'description_EN', 'name_AR', 'description_AR', 'name_FR', 'description_FR', 'is_active', 'min_price', 'service']

class SubserviceImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Subservice
        fields = ['image_light', 'image_dark']
