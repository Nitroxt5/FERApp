from django.urls import path

from .views import index, image_upload_recognize


urlpatterns = [
    path('', index, name='main'),
    path('upload/', image_upload_recognize, name='upload'),
]
