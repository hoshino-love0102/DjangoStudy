from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_form, name='hello_form'),
]