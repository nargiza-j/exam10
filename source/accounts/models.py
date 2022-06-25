from django.contrib.auth.models import AbstractUser

from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


class Users(AbstractUser):
    username = models.CharField(max_length=100, verbose_name='Имя пользователя', unique=True)
    first_name = models.CharField(max_length=150, verbose_name='Имя')
    phone = PhoneNumberField(region="KG", max_length=15, verbose_name='Номер телефона')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
