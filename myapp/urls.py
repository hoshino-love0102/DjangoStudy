from django.urls import path
from . import hello_view

urlpatterns = [
    path('', hello_view.hello, name='hello'),
]