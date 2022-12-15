from django.contrib.auth.models import AbstractUser
from django.db import models


class Photo(models.Model):

    image = models.ImageField(
        verbose_name='Фотография',
        help_text='Загрузите фотографию',
        upload_to='images/',
    )
    latitude = models.DecimalField(
        verbose_name='Широта',
        help_text='Введите широту',
        max_digits=8,
        decimal_places=6,
        null=True,
        blank=True,
    )
    longitude = models.DecimalField(
        verbose_name='Долгота',
        help_text='Введите долготу',
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True,
    )
    description = models.CharField(
        verbose_name='Описание',
        help_text='Введите описание фотографии',
        max_length=500,
        null=True,
        blank=True,
    )
    date = models.DateField(
        verbose_name='Дата создания/обновления',
    )
    people = models.CharField(
        verbose_name='Имена людей на фотографии',
        help_text='Введите имена людей на фотографии',
        max_length=500,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'Фотография {self.id}'

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
        ordering = ['-date']


class User(AbstractUser):

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
