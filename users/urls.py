from django.urls import path

from .views import CustomUserRegisterView

urlpatterns = [
    path('register/', CustomUserRegisterView.as_view(), name='register'),
]
