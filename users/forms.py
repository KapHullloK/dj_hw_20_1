from django.contrib.auth.forms import UserCreationForm

from users.models import User


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'country', 'password1', 'password2')