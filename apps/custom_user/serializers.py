from rest_framework import serializers

from .models import MyUser


class GetMyUserSerializer(serializers.ModelSerializer):
    """ Вывод информации о пользователе """

<<<<<<< HEAD
=======
    avatar = serializers.ImageField(read_only=True)

>>>>>>> 5dfeb0a (Added app followers: list and add.)
    class Meta:
        model = MyUser
        exclude = (
            "password",
            "last_login",
            "is_active",
            "is_staff",
            "is_superuser",
            "groups",
            "user_permissions",
        )


class GetMyUserPublicSerializer(serializers.ModelSerializer):
    """ Вывод публичной информации о пользователе """

    class Meta:
        model = MyUser
        exclude = (
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
<<<<<<< HEAD
=======


class MyUserToFollowerSerializer(serializers.ModelSerializer):
    """ Сериализация для подписчиков """

    avatar = serializers.ImageField(read_only=True)

    class Meta:
        model = MyUser
        fields = ('id', 'username', 'avatar')
>>>>>>> 5dfeb0a (Added app followers: list and add.)
