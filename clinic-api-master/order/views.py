from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.response import Response 
from .serializers import *
from .models import Order
from datetime import datetime
from rest_framework import status


@api_view(['GET'])
def OrdersList(request, pk):
    orders = Order.objects.filter(created_at__date=pk)
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def Total(request, pk):
    if pk == 'month':
        orders = Order.objects.filter(created_at__month=datetime.today().month)
        total = 0
        for order in orders:
            total = total + order.amount
        return Response(total)
    elif pk == 'year':
        orders = Order.objects.filter(created_at__year=datetime.today().year)
        total = 0
        for order in orders:
            total = total + order.amount
        return Response(total)
    else:
        orders = Order.objects.filter(created_at__date=pk)
        total = 0
        for order in orders:
            total = total + order.amount
        return Response(total)
    

@api_view(['POST'])
def CreateOrder(request):
    serializer = CreateOrderSerializer(data=request.data)
    
    if serializer.is_valid():
        patient = Patient.objects.get(id=request.data['patient'])
        patient.rest = patient.rest - request.data['amount']
        patient.save()
        serializer.save()
    return Response(serializer.data)

        