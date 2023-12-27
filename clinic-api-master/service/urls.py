from django.urls import path
from . import views


urlpatterns = [
    #admin
        ## service
        path('create', views.CreateService),
        path('<str:pk>/update', views.UpdateService),
        path('<str:pk>/delete', views.DeleteService),
        path('<str:pk>/uploadImage', views.UploadImageService),
        ## subservice
        path('subservice', views.ListOfSubservice),
        path('subservice/create', views.CreateSubservice),
        path('subservice/<str:pk>/uploadImage', views.UploadImageSubservice),
        path('subservice/<str:pk>/update', views.UpdateSubservice),
        path('subservice/<str:pk>/delete', views.DeleteSubservice),
    # Service
    path('', views.ListOfService),
    path('<str:pk>', views.OneService),
    # Subservice
    path('subservice/<str:pk>', views.OneSubservice),
    path('<str:pk>/subservice', views.SubserviceByServise),
]