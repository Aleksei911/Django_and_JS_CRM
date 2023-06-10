from .views import RegistrationView, UsernameValidationView, EmailValidationView
from django.urls import path


urlpatterns = [
    path('register', RegistrationView.as_view(), name='register'),
    path('validate-username', UsernameValidationView.as_view(), name='validate-username'),
    path('validate-email', EmailValidationView.as_view(), name='validate-email'),
]

