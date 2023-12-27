from rest_framework import serializers
from .models import *
from core.models import User
from django.db import transaction
from service.models import *

class OrderSerializer(serializers.ModelSerializer):


    customer = serializers.SerializerMethodField('get_customer_data')
    def get_customer_data(self, obj):
        data = {
            'first_name': obj.customer.first_name,
            'last_name': obj.customer.last_name,
            'phone': obj.customer.phone
        }
        return data
    
    subservice = serializers.SerializerMethodField('get_subservice_data')
    service = serializers.SerializerMethodField('get_service_data')

    def get_service_data(self, obj):
        
        data = {
            'image_light': obj.subservice.first().service.image_light.name,
            'image_dark': obj.subservice.first().service.image_dark.name,
            'name_en': obj.subservice.first().service.name_EN,
            'name_ar': obj.subservice.first().service.name_AR,
            'name_fr': obj.subservice.first().service.name_FR
        }
        return data


    
    def get_subservice_data(self, obj):
        data = []
        for i in obj.subservice.all():
            names = {
                'name_en': i.name_EN,
                'name_ar': i.name_AR,
                'name_fr': i.name_FR,
                'id': i.id
            }
            data.append(names)
        return data
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    class Meta:
        model = Order
        fields = ['id','customer','subservice','scheduled','location','price','state', 'service','created_at']

class CreateOrderSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    class Meta:
        model = Order
        fields = ['subservice','scheduled','location','price', 'id']

    def save(self, **kwargs):
        with transaction.atomic():
            (customer_id, create) = User.objects.only('id').get_or_create(id=self.context['user_id'])
            order_create = Order.objects.create(customer = customer_id)
            order = Order.objects.filter(id = order_create.id).first()
            self.validated_data['id'] = order_create.id
            sub = self.validated_data['subservice']
            for i in sub:
                order.subservice.add(i)
            order.scheduled = self.validated_data['scheduled']
            order.location = self.validated_data['location']
            order.price = self.validated_data['price']
            order.save()

class UpdateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['state']
