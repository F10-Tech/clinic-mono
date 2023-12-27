
# get 

def get(requset, Serializer, Object, pk):

    if pk:
        service = Service.objects.get(id= pk)
        subservice = Subservice.objects.filter( service = service)
        if requset.user.is_staff:
            service = Service.objects.get(id = pk)
            serializer = ServiceSerializer(service, many=False)
            return Response(serializer.data)
        else:
            service = Service.objects.get(id = pk, is_active = True)
            serializer = Serializer(object, many=False)
            return Response(serializer.data)
    else: 
        
        if requset.user.is_staff:
            serializer = Serializer(Object, many=True)
            return Response(serializer.data)
        else:
            service = Service.objects.filter(is_active = True)
            serializer = Serializer(Object, many=True)

            return Response(serializer.data)    



def post(requset, serializer):
    

    if serializer.is_valid():
            serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors,  status=status.HTTP_400_BAD_REQUEST)