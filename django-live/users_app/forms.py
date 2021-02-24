from django.forms import ModelForm
# For registration form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username',
                  'email',
                  'password1',
                  'password2'
                  ]

        # widgets = {
        #     'username': forms.TextInput(attrs={
        #         'class': 'form-control'
        #     }),
        #
        #     'email': forms.EmailInput(attrs={
        #         'class': 'form-control'
        #     })
        # }
