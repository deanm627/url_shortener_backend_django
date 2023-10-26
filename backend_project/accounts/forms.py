from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm

from .models import CustomUser

class NewUserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "username", "password", "email")

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "username", "password", "email")

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "username", "password", "email")