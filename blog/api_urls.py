from django.urls import path
from . import api_views

urlpatterns = [
    path("posts/", api_views.api_post_create, name="api_post_create"),
    path("posts/<int:pk>/", api_views.api_post_delete, name="api_post_delete"),
]
