from django.urls import path
from . import views

urlpatterns = [
    path('<str:pk>', views.OrdersList),
    path('total/<str:pk>', views.Total),
    path('create/', views.CreateOrder),
    path('<str:pk>/delete', views.DeleteOrder),
    path('<str:pk>/update', views.UpdateOrder),
]