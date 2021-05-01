from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from .models import *
from PIL import Image

class CreateUserForm(UserCreationForm):
    """user signup form"""
    email = forms.EmailField()
    name = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ('email', 'name', 'main', 'image_url', 'company', 'role', 'password1', 'password2',)
        # '__all__'
        exclude = ('created_at', 'updated_at', 'is_superadmin', 'is_active', 'is_staff', )


class LoginForm(forms.Form):
    """user login form"""
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
