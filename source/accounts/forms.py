from django import forms

from django.contrib.auth.forms import UserCreationForm, UsernameField
from phonenumber_field.formfields import PhoneNumberField

from accounts.models import Users


class MyUserCreationForm(UserCreationForm):
    phone = PhoneNumberField(
        error_messages={"invalid": "Формат: +996 XXX XXX XXX"})

    class Meta:
        model = Users
        fields = ['username', 'password1', 'password2',
                  'first_name', 'phone']
        field_classes = {'username': UsernameField}


class ProfileUpdateForm(forms.ModelForm):
    phone = PhoneNumberField(
        error_messages={"invalid": "Формат: +996 XXX XXX XXX"})

    class Meta:
        model = Users
        fields = ("phone",)