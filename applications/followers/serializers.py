from rest_framework import serializers

from custom_user.serializers import MyUserToFollowerSerializer
from .models import Follower


class ListFollowerSerializer(serializers.ModelSerializer):
    """ Сериализотор списка подписчиков """

    subscribers = MyUserToFollowerSerializer(many=True, read_only=True)

    class Meta:
        model = Follower
        fields = ('subscribers', )
