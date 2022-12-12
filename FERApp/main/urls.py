from django.urls import path

from .views import index, image_upload_recognize, image_download


urlpatterns = [
    path('', index, name='main'),
    path('upload/', image_upload_recognize, name='upload'),
    path('download/', image_download, name='download')
]
