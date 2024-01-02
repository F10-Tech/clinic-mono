import math
from rest_framework import serializers
from .models import *
import datetime

# Service

class PatientSerializer(serializers.ModelSerializer):

    status = serializers.SerializerMethodField('get_state_data')
    city = serializers.SerializerMethodField('get_city_data')
    regiment = serializers.SerializerMethodField('get_regiment_data')
    disease = serializers.SerializerMethodField('get_disease_data')
    sessions = serializers.SerializerMethodField('get_sessions_data')
    presence = serializers.SerializerMethodField('get_presence_data')

    def get_sessions_data(self, obj):
        presence = Presence.objects.filter(patient=obj.id)
        if obj.price != None:
            price = Price.objects.get(id = obj.price.id)
            if presence.count() == 0 and obj.rest == 0:
                return obj.number_of_days
            if presence.count() > 0:
                return math.floor( ( obj.number_of_days - (obj.rest / price.price ))  - presence.count())
        return 0
        
       
        # obj.rest =  presence.count() * obj.price.price
        return (presence.count() - obj.rest) / price.price

    def get_state_data(self, obj):
        if obj.number_of_days == 0:
            obj.regiment = None
            obj.save()
            return "CANCELLED"
        elif obj.number_of_days < 4 and obj.number_of_days > 0:
            return "IN_PROGRESS"
        else:
            return "COMPLETED"

    def get_disease_data(self, obj):
        if obj.disease != None:
            disease = Disease.objects.get(id=obj.disease.id)
            serializer = DiseaseSerializer(disease, many=False)
            return serializer.data
        return None

    def get_regiment_data(self, obj):
        if obj.regiment != None: 
            regiment = Regiment.objects.get(id=obj.regiment.id)
            serializer = RegimentSerializer(regiment, many=False)
            return serializer.data
        return None

    def get_city_data(self, obj):
        if obj.city != None:
            city = City.objects.get(id=obj.city.id)
            serializer = FullCitySerializer(city, many=False)
            return serializer.data
        return None

    def get_presence_data(self, obj):
        presence = Presence.objects.filter(patient=obj.id)
        serializer = DatePresenceSerializer(presence, many=True)
        return serializer.data
    
    class Meta:
        model = Patient
        fields = '__all__'


class ListPatientByRegimentSerializer(serializers.ModelSerializer):

    status = serializers.SerializerMethodField('get_state_data')
    city = serializers.SerializerMethodField('get_city_data')
    regiment = serializers.SerializerMethodField('get_regiment_data')
    disease = serializers.SerializerMethodField('get_disease_data')
    presence = serializers.SerializerMethodField('get_presence_data')
    checkout = serializers.SerializerMethodField('get_checkout_data')
    sessions = serializers.SerializerMethodField('get_sessions_data')

    def get_sessions_data(self, obj):
        presence = Presence.objects.filter(patient=obj.id)
        if obj.price != None:
            price = Price.objects.get(id = obj.price.id)
            if presence.count() == 0 and obj.rest == 0:
                return obj.number_of_days
            if presence.count() > 0:
                return math.floor( ( obj.number_of_days - (obj.rest / price.price ))  - presence.count())
        return 0


    def get_checkout_data(self, obj):
        presence = Presence.objects.filter(patient=obj.id, created_at__date = datetime.datetime.today().date() )
        serializer = DatePresenceSerializer(presence, many=True)
        if serializer.data:
            return True
        return False
        

    def get_state_data(self, obj):
        if obj.number_of_days == 0:
            obj.regiment = None
            obj.save()
            return "CANCELLED"
        elif obj.number_of_days < 4 and obj.number_of_days > 0:
            return "IN_PROGRESS"
        else:
            return "COMPLETED"

    def get_disease_data(self, obj):
        if obj.disease != None:
            disease = Disease.objects.get(id=obj.disease.id)
            serializer = DiseaseSerializer(disease, many=False)
            return serializer.data
        return None

    def get_regiment_data(self, obj):
        if obj.regiment != None:
            regiment = Regiment.objects.get(id=obj.regiment.id)
            serializer = RegimentSerializer(regiment, many=False)
            return serializer.data
        return None

    def get_city_data(self, obj):
        if obj.city != None:
            city = City.objects.get(id=obj.city.id)
            serializer = FullCitySerializer(city, many=False)
            return serializer.data
        return None

    def get_presence_data(self, obj):
        presence = Presence.objects.filter(patient=obj.id)
        serializer = DatePresenceSerializer(presence, many=True)
        return serializer.data
    
    class Meta:
        model = Patient
        fields = ['id', 'name', 'age', 'phone', 'number_of_days', 'regiment', 'disease', 'city', 'rest', 'sessions', 'status', 'checkout', 'presence']

class FullCitySerializer(serializers.ModelSerializer):

    # state = serializers.SerializerMethodField('get_state_data')
    # replace state.id  with state.name
    state = serializers.SerializerMethodField('get_state_data')

    def get_state_data(self, obj):
        if obj.state != None:
            state = State.objects.get(id=obj.state.id)
            return state.name
        return None

    class Meta:
        model = City
        fields = ['id', 'name', 'state']

class CreatePatientSerializer(serializers.ModelSerializer):


    class Meta:
        model = Patient
        fields = ['id', 'name', 'age', 'phone', 'medical_operation_date', 'doctor', 'number_of_days', 'regiment', 'disease', 'other_diseases', 'city', 'rest']

class UpdatePatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = ['name', 'age', 'phone', 'medical_operation_date', 'doctor', 'number_of_days', 'regiment', 'disease', 'other_diseases', 'city']

class UpdateImgsSerializer(serializers.ModelSerializer):
    
        class Meta:
            model = Patient
            fields = ['img_1','img_2']

class PresenceSerializer(serializers.ModelSerializer):
    patient = serializers.SerializerMethodField('get_patient_data')
    day = serializers.SerializerMethodField('get_day_data')

    def get_day_data(self, obj):
        return obj.created_at.today().strftime("%A")
    def get_patient_data(self, obj):
        return  obj.patient.name
    
    class Meta:
        model = Presence
        fields = ['patient', 'created_at', 'id', 'day']

class DatePresenceSerializer(serializers.ModelSerializer):
    day = serializers.SerializerMethodField('get_day_data')

    def get_day_data(self, obj):
        return obj.created_at.today().strftime("%A")
    
    class Meta:
        model = Presence
        fields = ['day','created_at' ,'id']

class CreatePresenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Presence
        fields = ['patient']


class DiseaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Disease
        fields = '__all__'

class CreateDiseaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Disease
        fields = ['name']

class StateSerializer(serializers.ModelSerializer):

    class Meta:
        model = State
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = '__all__'

class CreateStateSerializer(serializers.ModelSerializer):

    class Meta:
        model = State
        fields = ['name']

class CreateCitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ['name', 'state']

class RegimentSerializer(serializers.ModelSerializer):
    
        class Meta:
            model = Regiment
            fields = ['id', 'name','days']

class CreateRegimentSerializer(serializers.ModelSerializer):
    
        class Meta:
            model = Regiment
            fields = ['name','days']

class PriceSerializer(serializers.ModelSerializer):
    
        class Meta:
            model = Price
            fields = '__all__'