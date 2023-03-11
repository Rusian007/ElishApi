from .models import CustomUser
from django import forms
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label='email')  
    class Meta:
        model = CustomUser
        fields = '__all__'