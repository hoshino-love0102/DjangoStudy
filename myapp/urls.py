from django.urls import path
from .views import upload_view, show_photos

urlpatterns = [
    path('', upload_view, name='upload'),
    path('photos/', show_photos, name='photo_list'),
]