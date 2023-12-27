from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.response import Response 
from core.models import User
from .serializers import *
from .models import Order
from .operations import Change, Get


@api_view(['GET'])
def OneOrder(request, pk):
    return Get(request, OrderSerializer, Order.objects.get(id = pk), pk, False)

@api_view(['GET'])
def ChangeStateToPending(request,pk):
    return Change(Order.objects.get(id = pk), OrderSerializer, pk, 'PENDING')

@api_view(['GET'])
def ChangeStateToInProgress(request,pk):
    if request.user.is_staff:
        return Change(Order.objects.get(id = pk), OrderSerializer, pk, 'INPROGRESS')
    else:
        return Response('No permission')

@api_view(['GET'])
def ChangeStateToCompleted(request,pk):
    if request.user.is_staff:
        return Change(Order.objects.get(id = pk), OrderSerializer, pk, 'COMPLETED')
    else:
        return Response('No permission')

@api_view(['GET'])
def ChangeStateToReject(request,pk):
    return Change(Order.objects.get(id = pk), OrderSerializer, pk, 'REJECTED')

@api_view(['GET'])
def ChangeStateToCanceled(request,pk):
    return Change(Order.objects.get(id = pk), OrderSerializer, pk, 'CANCELLED')

@api_view(['GET'])
def ListOfOrderByCustomer(request,pk):
    return Get(request, OrderSerializer, Order.objects.filter(customer = pk), pk, True)

class OrderViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateOrderSerializer
        elif self.request.method == 'PATCH':
            return UpdateOrderSerializer
        return OrderSerializer
    
    def list(self, request):
        if request.user.is_staff:
            queryset = Order.objects.all()
        else:
            queryset = Order.objects.filter(customer = request.user.id)
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_serializer_context(self):
        return {'user_id': self.request.user.id}

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Order.objects.all()
        
        (customer_id, create) = User.objects.only('id').get_or_create(id = user.id)
        return Order.objects.filter(customer = customer_id)   