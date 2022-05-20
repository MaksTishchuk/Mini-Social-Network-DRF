from django.urls import path
from .views import FollowerCDView, ListFollowerView


urlpatterns = [
    path('<int:pk>/', FollowerCDView.as_view()),
    path('', ListFollowerView.as_view()),
]
