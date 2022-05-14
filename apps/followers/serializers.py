from rest_framework import serializers
from apps.custom_user.serializers import MyUserToFollowerSerializer
from .models import Follower


class ListFollowerSerializer(serializers.ModelSerializer):
    """ Сериализотор списка подписчиков """

    subscriber = MyUserToFollowerSerializer(many=True, read_only=True)

    model = Follower
    fields = ('subscriber', )
