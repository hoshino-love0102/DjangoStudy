from django.shortcuts import render, redirect
from .forms import PhotoForm
from .models import Photo

def upload_view(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('photo_list')
    else:
        form = PhotoForm()
    return render(request, 'myapp/upload.html', {'form': form})

def show_photos(request):
    photos = Photo.objects.order_by('-uploaded_at')
    return render(request, 'myapp/photo_list.html', {'photos': photos})