from rest_framework import serializers
from .models import *
import datetime


class OrderSerializer(serializers.ModelSerializer):

    patient = serializers.SerializerMethodField('get_patient_data')

    def get_patient_data(self, obj):
        if obj.patient is None:
            return 'تم حذف المريض'
        date = {
            'id': obj.patient.id,
            'name': obj.patient.name
        }
        return date
    

    class Meta:
        model = Order
        fields = '__all__'

class CreateOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'