from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListOfPatient),

    path('create', views.CreatePatient),
    path('delete/<str:pk>', views.DeletePatient),
    path('update/<str:pk>', views.UpdatePatient),
    path('<str:pk>/uploadImage', views.UpdateImgs),

    path('<str:pk>', views.DetailPatient),
    path('regiment/', views.ListOfPatientByRegiment),


    path('presence/<str:pk>', views.ListOfPresence),
    path('create/presence', views.CreatePresence),
    path('delete/presence/<str:pk>', views.DeletePresence),

    path('disease/', views.ListOfDisease),
    path('create/disease', views.CreateDisease),
    path('delete/disease/<str:pk>', views.DeleteDisease),


    path('city/', views.ListOfCity),
    path('create/city', views.CreateCity),
    path('delete/city/<str:pk>', views.DeleteCity),

    path('state/', views.ListOfState),
    path('create/state', views.CreateState),
    path('delete/state/<str:pk>', views.DeleteState),

    # path('regiment/', views.ListOfRegiment),
    path('create/regiment', views.CreateRegiment),
    path('delete/regiment/<str:pk>', views.DeleteRegiment),

]