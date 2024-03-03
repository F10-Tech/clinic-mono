from rest_framework.response import Response 
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Patient
from core.permissions import IsServiceAdmin
from datetime import datetime
from rest_framework import status

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def ListOfPatient(request):
    patient = Patient.objects.all()
    serializer = PatientSerializer(patient, many=True)
    return Response(serializer.data)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def DetailPatient(request, pk):
    patient = Patient.objects.get(id=pk)
    serializer = PatientSerializer(patient, many=False)
    return Response(serializer.data)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def ListOfPatientByRegimentID(request, pk):
    
    patients = Patient.objects.filter(regiment=pk)
    serializer = PatientSerializer(patients, many=True)
    return Response(serializer.data)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def ListOfPatientByRegiment(request):
    current_datetime = datetime.now()
    hour = current_datetime.hour - 1
    regiments = Regiment.objects.all()
    for regiment in regiments:
        if regiment.period == 'MORNING' and hour <= 12:
            print('MORNING')
            for day in regiment.days.all():
                if day.name == datetime.today().strftime("%A"):
                    patients = regiment.patient_set.all()
                    serializer = ListPatientByRegimentSerializer(patients, many=True)
                    return Response(serializer.data)
        elif regiment.period == 'EVENING' and hour > 12:
            for day in regiment.days.all():
                if day.name == datetime.today().strftime("%A"):
                    patients = regiment.patient_set.all()
                    serializer = ListPatientByRegimentSerializer(patients, many=True)
                    return Response(serializer.data)
    return Response(status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def CreatePatient(request):
    if request.data['price'] != None:
        price = Price.objects.get(id=request.data['price'])
        request.data['rest'] = price.price * request.data['number_of_days']

    serializer = CreatePatientSerializer(data=request.data)

    if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
def DeletePatient(request, pk):
    patient = Patient.objects.get(id=pk)
    patient.delete()
    return Response('Patient was deleted')

@api_view(['PATCH'])
# @permission_classes([IsAuthenticated])
def UpdatePatient(request, pk):
    if request.data['price'] != None:
        patient = Patient.objects.get(id=pk)
        if patient.number_of_days < request.data['number_of_days'] :
            price = Price.objects.get(id=request.data['price'])
            request.data['rest'] =  patient.rest + (price.price * ( request.data['number_of_days']  - patient.number_of_days ))
        elif patient.number_of_days > request.data['number_of_days'] :
            price = Price.objects.get(id=request.data['price'])
            request.data['rest'] =  patient.rest - (price.price * ( patient.number_of_days  -  request.data['number_of_days'] ))
        
    patient = Patient.objects.get(id=pk)
    serializer = UpdatePatientSerializer(patient, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def UpdateImgs(request, pk):
    patient = Patient.objects.get(id=pk)
    serializer = UpdateImgsSerializer(patient, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def ListOfPresence(request, pk):
    if pk == 'today':
        presence = Presence.objects.filter(created_at__date=datetime.today())


    else:
        presence = Presence.objects.filter(created_at__date=pk)

    serializer = PresenceSerializer(presence, many=True)
    return Response(serializer.data)

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def CreatePresence(request):
    serializer = CreatePresenceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
def DeletePresence(request, pk):
    presence = Presence.objects.get(id=pk)
    serializer = PresenceSerializer(presence, many=False)
    presence.delete()
    return Response(serializer.data)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def ListOfDisease(request):
    disease = Disease.objects.all()
    serializer = DiseaseSerializer(disease, many=True)
    return Response(serializer.data)

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def CreateDisease(request):
    serializer = CreateDiseaseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
def DeleteDisease(request, pk):
    disease = Disease.objects.get(id=pk)
    serializer = DiseaseSerializer(disease, many=False)
    disease.delete()
    return Response(serializer.data)

# State and City

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def ListOfState(request):
    state = State.objects.all()
    serializer = StateSerializer(state, many=True)
    return Response(serializer.data)

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def CreateState(request):
    serializer = CreateStateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
def DeleteState(request, pk):
    state = State.objects.get(id=pk)
    serializer = StateSerializer(state, many=False)
    state.delete()
    return Response(serializer.data)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def ListOfCity(request):
    city = City.objects.all()
    serializer = CitySerializer(city, many=True)
    return Response(serializer.data)

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def CreateCity(request):
    serializer = CreateCitySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
def DeleteCity(request, pk):
    city = City.objects.get(id=pk)
    serializer = CitySerializer(city, many=False)
    city.delete()
    return Response(serializer.data)


# Regiment

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def ListOfRegiment(request):
    regiment = Regiment.objects.all()
    serializer = RegimentSerializer(regiment, many=True)
    return Response(serializer.data)

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def CreateRegiment(request):
    serializer = CreateRegimentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
def DeleteRegiment(request, pk):
    regiment = Regiment.objects.get(id=pk)
    serializer = RegimentSerializer(regiment, many=False)
    regiment.delete()
    return Response(serializer.data)

@api_view(['PATCH'])
# @permission_classes([IsAuthenticated])
def UpdateRegiment(request, pk):
    regiment = Regiment.objects.get(id=pk)
    serializer = RegimentSerializer(regiment, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def ListOfDays(request):
    days = Day.objects.all()
    serializer = DaySerializer(days, many=True)
    return Response(serializer.data)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def ListOfPrice(request):
    price = Price.objects.all()
    serializer = PriceSerializer(price, many=True)
    return Response(serializer.data) 

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def CreatePrice(request):
    serializer = PriceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
def DeletePrice(request, pk):
    price = Price.objects.get(id=pk)
    serializer = PriceSerializer(price, many=False)
    price.delete()
    return Response(serializer.data)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def ListOfDoctor(request):
    doctor = Doctor.objects.all()
    serializer = DoctorSerializer(doctor, many=True)
    return Response(serializer.data) 

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def CreateDoctor(request):
    serializer = DoctorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
def DeleteDoctor(request, pk):
    doctor = Doctor.objects.get(id=pk)
    serializer = DoctorSerializer(doctor, many=False)
    doctor.delete()
    return Response(serializer.data)