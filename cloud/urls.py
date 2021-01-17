from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/list', views.api_image_list, name="api_image_list"),
    path('upload/', views.upload_image, name='upload_image'),
    path('list/',views.image_list, name='image_list'),
    path('api/download/<int:pk>', views.file_download, name='file_download'),
    path('delete/<int:pk>/', views.delete_file, name='delete_file'),
]