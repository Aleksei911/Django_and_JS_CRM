from .views import RegistrationView, UsernameValidationView, EmailValidationView, VerificationView, LoginView, \
    LogoutView
from django.urls import path

urlpatterns = [
    path('register', RegistrationView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('validate-username', UsernameValidationView.as_view(), name='validate-username'),
    path('validate-email', EmailValidationView.as_view(), name='validate-email'),
    path('activate/<uidb64>/<token>', VerificationView.as_view(), name='activate'),
]
