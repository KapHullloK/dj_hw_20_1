from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from dj_hw_20_1.settings import EMAIL_HOST_USER
from users.forms import UserRegistrationForm
from users.models import User

import secrets
import string
import random


def generate_random_password(length=10):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


def password_reset_request(request):
    if request.method == 'POST':
        try:
            email = request.POST.get('email')

            user = User.objects.get(email=email)
            new_password = generate_random_password()

            user.password = make_password(new_password)
            user.save()

            send_mail(
                subject="Восстановление пароля",
                message=f"Новый пароль:{new_password}",
                from_email=EMAIL_HOST_USER,
                recipient_list=[user.email],
            )

            return render(request, 'users/wait_reset.html', {'email': email})
        except User.DoesNotExist:
            return render(request, 'users/password_reset.html',
                          {'error': 'Пользователь с таким email не найден.'})
    return render(request, 'users/password_reset.html')


class RegisterView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()

        url = f'http://{self.request.get_host()}/users/confirm/{token}/'

        send_mail(
            subject="Подтверждение почты",
            message=f"ссылка для подтверждения почты:{url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )

        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))
