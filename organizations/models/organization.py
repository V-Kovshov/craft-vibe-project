from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Organization(models.Model):
    name = models.CharField(max_length=255, verbose_name='Назва організації', blank=False)
    owner = models.ForeignKey(
        to=User,
        on_delete=models.RESTRICT,
        related_name='organizations_owner',
        verbose_name='Керівник',
    )
    employees = models.ManyToManyField(
        to=User,
        related_name='organizations_employees',
        verbose_name='Співробітники',
        blank=True,
    )

    class Meta:
        verbose_name = 'Організація'
        verbose_name_plural = 'Організації'
        ordering = ['-id']
