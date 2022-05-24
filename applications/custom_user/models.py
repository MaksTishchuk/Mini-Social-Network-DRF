from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    """ Кастомная модель пользователя """

    GENDER = (
        ('male', 'male'),
        ('female', 'female')
    )

    middle_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Отчество')
    first_login = models.DateTimeField(
        blank=True, null=True, verbose_name='Дата подтверждения почты'
    )  # Дата подтверждения почты
    phone = models.CharField(max_length=14, blank=True, null=True, verbose_name='Телефон')
    avatar = models.ImageField(
        upload_to='user/avatar/%Y/%m/%d/', blank=True, null=True, verbose_name='Аватар'
    )
    biography = models.TextField(blank=True, null=True, verbose_name='Биография')
    github = models.CharField(
        max_length=500, blank=True, null=True, verbose_name='Ссылка на github'
    )
    birthday = models.DateField(blank=True, null=True, verbose_name='Дата рождения')
    gender = models.CharField(
        max_length=10, choices=GENDER, default='male', verbose_name='Пол'
    )
    technology = models.ManyToManyField(
        'Technology', related_name='users', blank=True, null=True, verbose_name='Технологии'
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['-id']


class Technology(models.Model):
    """ Технологии, которыми владеет пользователь """

    name = models.CharField(max_length=100, verbose_name='Наименование')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Технология'
        verbose_name_plural = 'Технологии'
        ordering = ['name']
