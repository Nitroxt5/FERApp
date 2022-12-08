from django.urls import path
from .views import index, log_in, log_out, register


urlpatterns = [
    path('', index, name='auth'),
    path('login/', log_in, name='login'),
    path('register/', register, name='register'),
    path('logout/', log_out, name='logout'),
]
