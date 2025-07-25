from django.shortcuts import render, redirect
from .forms import PhotoForm

def upload_view(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload')
    else:
        form = PhotoForm()
    return render(request, 'myapp/upload.html', {'form': form})