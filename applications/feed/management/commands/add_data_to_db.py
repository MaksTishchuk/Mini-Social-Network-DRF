from django.core.management.base import BaseCommand
from custom_user.models import MyUser
from followers.models import Follower
from wall.models import Post


class Command(BaseCommand):
    """
        Заполняем базу данных рандомными данными про проверки нагрузки на БД комнадой:
        python manage.py command
    """

    def handle(self, *args, **options):
        # self.create_user()
        # self.create_follower()
        self.create_post()
        self.stdout.write('Success')

    def create_user(self):
        """ Создаем новых случайных пользователей в БД """

        for i in range(10):
            user = MyUser.objects.create(
                username=f"test_{i + 1}",
                email=f"test_{i + 1}@gmail.com",
                is_active=True,
                middle_name=f"testovich-{i}",
                phone=f"1234567890{i}",
                gender=1
            )
            user.set_password('maksmaksmaks')
            user.save()

    def create_follower(self):
        """ Создаем новых случайных подписчиков в БД """

        user_list = MyUser.objects.order_by()[2:]
        for user in user_list:
            Follower.objects.create(user=user, subscriber_id=1)

    def create_post(self):
        """ Создаем новые посты в БД """

        user_list = MyUser.objects.all()
        for user in user_list:
            for i in range(10):
                Post.objects.create(text=f"Test post {i} for test DB", user=user)
