from django.urls import path
from . import views

urlpatterns = [
    # patient/
    path('', views.ListOfPatient),
    path('create', views.CreatePatient),
    path('<str:pk>/delete', views.DeletePatient),
    path('<str:pk>/update', views.UpdatePatient),
    path('<str:pk>/uploadImage', views.UpdateImgs),
    path('<str:pk>', views.DetailPatient),
    path('byregiment/', views.ListOfPatientByRegiment),

    # presence/
    path('presence/<str:pk>', views.ListOfPresence),
    path('presence/create', views.CreatePresence),
    path('presence/<str:pk>/delete', views.DeletePresence),

    # disease/
    path('disease/', views.ListOfDisease),
    path('disease/create', views.CreateDisease),
    path('disease/delete/<str:pk>', views.DeleteDisease),

    # city/
    path('city/', views.ListOfCity),
    path('city/create', views.CreateCity),
    path('city/<str:pk>/delete', views.DeleteCity),

    # state/
    path('state/', views.ListOfState),
    path('state/create', views.CreateState),
    path('state/delete/<str:pk>', views.DeleteState),

    # regiment/
    path('regiment/', views.ListOfRegiment),
    path('regiment/create', views.CreateRegiment),
    path('regiment/<str:pk>/delete', views.DeleteRegiment),

]