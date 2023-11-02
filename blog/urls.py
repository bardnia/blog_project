from django.urls import path
from . import views


urlpatterns = [
    path('', views.postlist, name='postlist'),
    path('top/', views.post_top, name='post_top'),
    path('write/', views.post_write, name='post_write'),
    path('<int:pk>/', views.postdetail, name='postdetail'),
    path('edit/<int:pk>/', views.post_edit, name='post_edit'),
    path('delete/<int:pk>/', views.post_delete, name='post_delete'),
    path('tag/<str:tag>/', views.posttag, name='posttag'),
]