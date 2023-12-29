from rest_framework import serializers
from .models import *

# Service

class PatientSerializer(serializers.ModelSerializer):

    status = serializers.SerializerMethodField('get_state_data')
    city = serializers.SerializerMethodField('get_city_data')
    regiment = serializers.SerializerMethodField('get_regiment_data')
    disease = serializers.SerializerMethodField('get_disease_data')
    # other_diseases = serializers.SerializerMethodField('get_other_diseases_data')
    presence = serializers.SerializerMethodField('get_presence_data')

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

class FullCitySerializer(serializers.ModelSerializer):

    state = serializers.SerializerMethodField('get_state_data')

    def get_state_data(self, obj):
        state = State.objects.get(id=obj.state.id)
        serializer = CreateStateSerializer(state, many=False)
        return serializer.data

    class Meta:
        model = City
        fields = ['id', 'name', 'state']

class CreatePatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = ['name', 'age', 'phone', 'medical_operation_date', 'doctor', 'number_of_days', 'regiment', 'disease', 'other_diseases', 'city']

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

    def get_patient_data(self, obj):
        
        data = {
            'name': obj.patient.name,
            'phone': obj.patient.phone,
            'number_of_days': obj.patient.number_of_days,

        }
        return data
    
    class Meta:
        model = Presence
        fields = ['patient', 'created_at']

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