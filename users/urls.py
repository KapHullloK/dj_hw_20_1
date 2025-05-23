from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, email_verification, password_reset_request

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registr/', RegisterView.as_view(), name='register'),
    path('confirm/<str:token>/', email_verification, name='email_verification'),
    path('reset_password/', password_reset_request, name='reset_password'),
]
