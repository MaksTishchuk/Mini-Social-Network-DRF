from django.conf import settings
from django.db import models


class Follower(models.Model):
    """ Модель подписчиков """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owner'
    )  # Тот, на кого подписываются
    subscriber = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='followers'
    )  # Тот, кто подписывается
