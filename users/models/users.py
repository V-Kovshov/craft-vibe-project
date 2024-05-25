from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

from users.managers import CustomUserManager


class User(AbstractUser):
    phone_number = PhoneNumberField('Номер телефону', unique=True, null=True)

    # USERNAME_FIELD = ''
    # REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Користувач'
        verbose_name_plural = 'Користувачі'

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

