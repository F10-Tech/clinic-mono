from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response 
from .serializers import UserSerializer
from .permissions import IsServiceAdmin
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from .forms import ResetPassword
from django.views import View
from .models import User
import requests
import json

       
class ResetPasswordView(View):
    def get(self, request, uid, token):
        form = ResetPassword()
        print(uid, token)
        return render(request, 'password_reset_email.html', {"form": form})

    def post(self, request, uid, token):
        form = ResetPassword(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data["new_password"]
            re_new_password = form.cleaned_data["re_new_password"]
            print("new_password : ", new_password)
            print("re_new_password: ", re_new_password)
            if new_password == re_new_password:
                payload = {
                    'uid': uid,
                    'token': token,
                    'new_password': new_password,
                    're_new_password': re_new_password,
                }
                headers = {'Content-Type': 'application/json'}
                protocol = 'https://' if request.is_secure() else 'http://'
                web_url = protocol + request.get_host() + '/'
                password_reset_url = "auth/users/reset_password_confirm/"

                password_post_url = web_url + password_reset_url
                response = requests.post(password_post_url, data=json.dumps(payload), headers=headers)
                print(response.status_code)

                if response.status_code == 204:
                    return render(request, 'completed_reset.html')
                elif response.status_code == 400:
                    return render(request, 'error_reset.html')
            else:
                print('Passwords do not match')
                form.add_error('re_new_password', 'Passwords do not match')
        else:
            form.add_error('re_new_password', 'Passwords do not match')

        return render(request, 'password_reset_email.html', {"form": form})
    

@api_view(['GET'])
@permission_classes([IsServiceAdmin])
def ListOfcustomers(request):
    users = User.objects.filter(is_staff=False)
    Serializer = UserSerializer(users, many=True)
    return HttpResponse(json.dumps(Serializer.data), content_type='application/json')

@api_view(['GET'])
@permission_classes([IsServiceAdmin])
def ListOfstaff(request):
    users = User.objects.filter(is_staff=True)
    Serializer = UserSerializer(users, many=True)
    return HttpResponse(json.dumps(Serializer.data), content_type='application/json')

@api_view(['PATCH'])
@permission_classes([IsServiceAdmin])
def UpdateUser(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    return Response(serializer.errors,  status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsServiceAdmin])
def DeleteUser(request, pk):
    user = User.objects.get(id=pk)
    user.delete()
    return Response('Object deleted')
