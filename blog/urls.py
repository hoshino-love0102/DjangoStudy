from django.urls import path
from . import views

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("post/new/", views.post_new, name="post_new"),

    path("post/<int:pk>/", views.post_detail, name="post_detail"),

    path("post/<int:pk>/delete/", views.post_delete, name="post_delete"),

    path("post/<int:pk>/comments/new/", views.comment_create, name="comment_create"),
    path("post/<int:pk>/comments/<int:comment_pk>/delete/", views.comment_delete, name="comment_delete"),
]
