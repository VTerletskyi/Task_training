from .models import User
from django.forms import ModelForm, TextInput


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['user_name', 'email', 'password']

        widgets = {
            "user_name": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ім'я"
        }),
            "email": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Електронна пошта"
            }),
            "password": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Пароль"
            })
        }
