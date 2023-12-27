from . import views
from django.urls import path, re_path
from .views import ResetPasswordView
from django.views.generic.base import TemplateView

urlpatterns = [
            path('password/reset/confirm/<uid>/<token>',ResetPasswordView.as_view()),
            path('users/customer', views.ListOfcustomers),
            path('users/staff', views.ListOfstaff),
            path('users/update/<int:pk>', views.UpdateUser),
            path('users/delete/<int:pk>', views.DeleteUser),

]
