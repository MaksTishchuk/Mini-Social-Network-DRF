from django.urls import path

from . import views


urlpatterns = [
    path('profile/', views.MyUserPrivateView.as_view()),
    path('profile/<int:pk>/', views.MyUserPublicView.as_view({'get': 'retrieve'})),
]
