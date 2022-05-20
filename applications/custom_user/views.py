from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from .models import MyUser
from .serializers import GetMyUserSerializer, GetMyUserPublicSerializer


class MyUserView(ModelViewSet):
    """ Вывод личного профиля пользователя """

    serializer_class = GetMyUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return MyUser.objects.filter(id=self.request.user.id)


class MyUserPublicView(ModelViewSet):
    """ Вывод публичного профиля пользователя """

    queryset = MyUser.objects.all()
    serializer_class = GetMyUserPublicSerializer
    permission_classes = [permissions.AllowAny]
