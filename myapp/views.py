from django.shortcuts import render
from django.http import HttpResponse

def hello_view(request):
    return HttpResponse("Hello, Django!")