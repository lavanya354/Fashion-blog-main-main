
from django.urls import path
from . import views

urlpatterns = [
    path('add_post/', views.add_post, name='add_post'),
    path('list_posts/', views.list_posts, name='list_posts'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
]
