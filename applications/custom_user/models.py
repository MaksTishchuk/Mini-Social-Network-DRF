from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUser(AbstractUser):
    """ Кастомная модель пользователя """

    GENDER = (
        ('male', 'male'),
        ('female', 'female')
    )

    middle_name = models.CharField(max_length=50)
    first_login = models.DateTimeField(blank=True, null=True)  # Дата подтверждения почты
    phone = models.CharField(max_length=14)
    avatar = models.ImageField(upload_to='user/avatar/%Y/%m/%d/', blank=True, null=True)
    biography = models.TextField(blank=True, null=True)
    github = models.CharField(max_length=500, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER, default='male')
    technology = models.ManyToManyField('Technology', related_name='users')


class Technology(models.Model):
    """ Технологии, которыми владеет пользователь """

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
