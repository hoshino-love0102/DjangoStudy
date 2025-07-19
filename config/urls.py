from django.contrib import admin
from django.urls import path, include  # include 추가

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # ✅ 루트 경로에 myapp 연결
]