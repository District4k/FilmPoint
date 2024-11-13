from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, get_user_model

User = get_user_model()


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        # username, password1 and password2 is built in functions
