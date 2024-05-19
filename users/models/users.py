from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    phone_number = PhoneNumberField('Номер телефону', unique=True, null=True)

    # USERNAME_FIELD = ''
    # REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Користувач'
        verbose_name_plural = 'Користувачі'

