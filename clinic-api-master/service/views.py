from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Service, Subservice
from core.permissions import IsServiceAdmin
from .operations import get, post, delete, patch



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def ListOfService(request):
    return get(request, ServiceSerializer, Service.objects.all(), None)
  
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def OneService(request, pk):
    return get(request, ServiceSerializer, Service.objects.get(id = pk), pk)
    
@api_view(['POST'])
@permission_classes([IsServiceAdmin])
def CreateService(request):
    return post(request, ServiceSerializer, None, None)

@api_view(['PATCH'])
@permission_classes([IsServiceAdmin])
def UpdateService(request,pk):
    return patch(request, UpdateServiceSerializer, Service.objects.get(id = pk))

@api_view(['POST'])
@permission_classes([IsServiceAdmin])
def UploadImageService(request, pk):
        return post(request, ServiceImageSerializer, pk, Service.objects.get(id = pk))

@api_view(['DELETE'])
@permission_classes([IsServiceAdmin])
def DeleteService(request,pk):
    return delete(Service.objects.get(id = pk), pk)

@api_view(['GET'])
@permission_classes([IsServiceAdmin])
def ListOfSubservice(request):
    return get(request, SubserviceSerializer, Subservice.objects.all(), None)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def OneSubservice(request, pk):
    return get(request, SubserviceSerializer, Subservice.objects.get(id = pk), pk)

@api_view(['POST'])
@permission_classes([IsServiceAdmin])
def CreateSubservice(request):
    return post(request, SubserviceSerializer, None, None)

@api_view(['PATCH'])
@permission_classes([IsServiceAdmin])
def UpdateSubservice(request, pk):
    return patch(request, UpdateSubserviceSerializer, Subservice.objects.get(id = pk))

@api_view(['POST'])
@permission_classes([IsServiceAdmin])
def UploadImageSubservice(request, pk):
        return post(request, SubserviceImageSerializer, pk, Subservice.objects.get(id = pk))

@api_view(['DELETE'])
@permission_classes([IsServiceAdmin])
def DeleteSubservice(request,pk):
    return delete(Subservice.objects.get(id = pk), pk)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def SubserviceByServise(request, pk):
    return get(request, SubserviceSerializer, Subservice.objects.filter( service = Service.objects.get(id= pk)), None)