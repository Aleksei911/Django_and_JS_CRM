from .views import RegistrationView, UsernameValidationView, EmailValidationView, VerificationView, LoginView
from django.urls import path


urlpatterns = [
    path('register', LoginView.as_view(), name='register'),
    path('login', RegistrationView.as_view(), name='login'),
    path('validate-username', UsernameValidationView.as_view(), name='validate-username'),
    path('validate-email', EmailValidationView.as_view(), name='validate-email'),
    path('activate/<uidb64>/<token>', VerificationView.as_view(), name='activate'),
]

