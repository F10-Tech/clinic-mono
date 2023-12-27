from django.urls import path
from django.urls.conf import include
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('', views.OrderViewSet, basename='orders')

urlpatterns = router.urls  + [
    path('<str:pk>', views.OneOrder),
    path('change/<str:pk>/pending', views.ChangeStateToPending),
    path('change/<str:pk>/inprogress', views.ChangeStateToInProgress),
    path('change/<str:pk>/completed', views.ChangeStateToCompleted),
    path('change/<str:pk>/reject', views.ChangeStateToReject ),
    path('change/<str:pk>/cancel', views.ChangeStateToCanceled),
    path('customer/<str:pk>', views.ListOfOrderByCustomer),
]
