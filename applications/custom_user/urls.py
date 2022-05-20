from django.urls import path

from . import views


urlpatterns = [
    path('profile/<int:pk>/', views.MyUserView.as_view({'get': 'retrieve', 'put': 'update'})),
    path('<int:pk>/', views.MyUserPublicView.as_view({'get': 'retrieve'})),
]
