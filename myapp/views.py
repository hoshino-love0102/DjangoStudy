from django.shortcuts import render

def hello_form(request):
    name = None

    if request.method == 'POST':
        name = request.POST.get('name')

    return render(request, 'myapp/hello_form.html', {'name': name})