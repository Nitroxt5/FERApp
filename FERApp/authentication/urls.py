from django.urls import path, include

from .views import index, login, register


urlpatterns = [
    path('', index),
    path('login/', login, name="login"),
    path('register/', register, name="register"),
]
