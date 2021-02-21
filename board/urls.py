from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    path('list/', views.post_list, name='post_list'),
    path('write/', views.post_write, name='post_write'),
    path('detail/<int:pk>/', views.post_detail, name='post_detail'),
]