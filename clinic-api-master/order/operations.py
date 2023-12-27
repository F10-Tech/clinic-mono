from rest_framework.response import Response 
from rest_framework import status


def Change(Object,Serializer,pk, State):
    Object.state = State
    Object.save()
    serializer = Serializer(Object, many=False)
    return Response(serializer.data)

def Get(request, Serializer, Object, pk,List, *args, **kwargs):
    if pk:
        if request.user.is_staff:
            if List:
                serializer = Serializer(Object, many=True)
            else:
                serializer = Serializer(Object, many=False)
            return Response(serializer.data)
        elif Object.customer == request.user:
            serializer = Serializer(Object, many=False)
        else:
            return Response('No permission')
    else:
        if request.user.is_staff:
            serializer = Serializer(Object, many=True)
    return Response(serializer.data)