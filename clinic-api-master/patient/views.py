from rest_framework.response import Response 
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Patient
from core.permissions import IsServiceAdmin
import datetime
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
def ListOfPatientByRegiment(request):
    regiments = Regiment.objects.all()
    for regiment in regiments:
        # print(datetime.datetime.today().strftime("%A"))
        for day in regiment.days.all():
            if day.name == datetime.datetime.today().strftime("%A"):
                print(day.name)
                patients = regiment.patient_set.all()
                serializer = PatientSerializer(patients, many=True)
                return Response(serializer.data)
    return Response(status.HTTP_400_BAD_REQUEST)

    # patient = Patient.objects.filter(regiment=pk)
    # serializer = DetailPatientSerializer(patient, many=True)
    # return Response(serializer.data)

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def CreatePatient(request):
    serializer = CreatePatientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
def DeletePatient(request, pk):
    patient = Patient.objects.get(id=pk)
    patient.delete()
    return Response('Patient was deleted')

@api_view(['PATCH'])
# @permission_classes([IsAuthenticated])
def UpdatePatient(request, pk):
    patient = Patient.objects.get(id=pk)
    serializer = UpdatePatientSerializer(patient, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def UpdateImgs(request, pk):
    patient = Patient.objects.get(id=pk)
    serializer = UpdateImgsSerializer(patient, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def ListOfPresence(request, pk):
    if pk == 'today':
        presence = Presence.objects.filter(created_at__date=datetime.datetime.today())


    else:
        presence = Presence.objects.filter(created_at__date=pk)

    serializer = PresenceSerializer(presence, many=True)
    return Response(serializer.data)

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def CreatePresence(request):
    patient = Patient.objects.get(id=request.data['patient'])
    patient.number_of_days = patient.number_of_days - 1
    patient.save()
    serializer = CreatePresenceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
def DeletePresence(request, pk):
    presence = Presence.objects.get(id=pk)
    patient = Patient.objects.get(id=presence)
    serializer = PresenceSerializer(presence, many=False)
    patient.number_of_days = patient.number_of_days + 1
    patient.save()
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
    return Response(status.HTTP_400_BAD_REQUEST)

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
    return Response(status.HTTP_400_BAD_REQUEST)

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
    return Response(status.HTTP_400_BAD_REQUEST)

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
    return Response(status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
def DeleteRegiment(request, pk):
    regiment = Regiment.objects.get(id=pk)
    serializer = RegimentSerializer(regiment, many=False)
    regiment.delete()
    return Response(serializer.data)