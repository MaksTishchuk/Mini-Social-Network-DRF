from django.conf import settings
from django.db import models


class Follower(models.Model):
    """ Модель подписчиков """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owner'
    )  # Тот, на кого подписываются
    subscriber = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='subscribers'
    )  # Тот, кто подписывается

    def __str__(self):
        return f'{self.subscriber} subscribe to {self.user}'
