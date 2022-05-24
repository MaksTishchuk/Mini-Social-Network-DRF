from django.conf import settings

from wall.models import Post


class Feed:
    """ Сервис получения списка постов пользователей, на которых мы подписаны """

    def get_post_list(self, user: settings.AUTH_USER_MODEL):
        return Post.objects.filter(
            user__owner__subscriber=user, published=True, moderation=True
        ).order_by('-create_date').select_related('user').prefetch_related('comments')

    def get_single_post(self, pk: int):
        return Post.objects.select_related('user').prefetch_related('comments').get(id=pk)


feed_service = Feed()
