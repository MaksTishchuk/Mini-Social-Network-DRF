from rest_framework import permissions, response
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet, generics, mixins

from .models import MyUser
from .serializers import GetMyUserSerializer, GetMyUserPublicSerializer


class MyUserPrivateView(generics.RetrieveUpdateAPIView):
    """ Вывод личного профиля пользователя """

    serializer_class = GetMyUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return MyUser.objects.filter(id=self.request.user.id)

    def get_object(self):
        obj = get_object_or_404(self.get_queryset())
        self.check_object_permissions(self.request, obj)
        return obj


class MyUserPublicView(ModelViewSet):
    """ Вывод публичного профиля пользователя """

    queryset = MyUser.objects.all()
    serializer_class = GetMyUserPublicSerializer
    permission_classes = [permissions.AllowAny]
