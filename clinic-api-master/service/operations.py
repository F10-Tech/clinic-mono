from rest_framework.response import Response 
from rest_framework import status

# GET

def get(request, Serializer, Object, pk, *args, **kwargs):

    if pk:
        if request.user.is_staff:
            serializer = Serializer(Object, many=False)
        else:
            list = Object.objects.get(id = pk, is_active = True)
            serializer = Serializer(list, many=False)

    else:
        if request.user.is_staff:
            serializer = Serializer(Object, many=True)
        else:
            list = Object.objects.filter(is_active = True)
            serializer = Serializer(list, many=True)

    return Response(serializer.data)

# POST

def post(request, Serializer, pk, Object, *args, **kwargs):

    if pk:
        serializer = Serializer(Object, data=request.data, partial=True)

    else:
        serializer = Serializer(data = request.data)


    if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors,  status=status.HTTP_400_BAD_REQUEST)

# DELETE

def delete(Object, pk):
        Object.delete()
        return Response('Object deleted')


# PATCH

def patch(request, Serializer, Object, *args, **kwargs):
         
        serializer = Serializer(Object, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,  status=status.HTTP_400_BAD_REQUEST)