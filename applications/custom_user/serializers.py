from rest_framework import serializers

from .models import MyUser


class GetMyUserSerializer(serializers.ModelSerializer):
    """ Вывод информации о пользователе """

    # avatar = serializers.ImageField(read_only=True)

    class Meta:
        model = MyUser
        exclude = (
            "id",
            "password",
            "email",
            "last_login",
            "is_active",
            "is_staff",
            "is_superuser",
            "groups",
            "user_permissions",
            "date_joined",
            "first_login",
            "avatar"
        )


class GetMyUserPublicSerializer(serializers.ModelSerializer):
    """ Вывод публичной информации о пользователе """

    class Meta:
        model = MyUser
        exclude = (
            "id",
            "email",
            "phone",
            "password",
            "last_login",
            "is_active",
            "is_staff",
            "is_superuser",
            "groups",
            "user_permissions",
        )


class MyUserToFollowerSerializer(serializers.ModelSerializer):
    """ Сериализация для подписчиков """

    avatar = serializers.ImageField(read_only=True)

    class Meta:
        model = MyUser
        fields = ('id', 'username', 'avatar')
