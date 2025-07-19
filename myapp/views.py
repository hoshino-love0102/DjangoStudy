from django.shortcuts import render
from .models import Guest

def hello_form(request):
    name = ''
    error = ''

    if request.method == 'POST':
        name_input = request.POST.get('name', '').strip()

        if not name_input:
            error = '이름을 입력해주세요.'
        elif name_input.lower() in ['admin', 'root', 'badword']:
            error = f'"{name_input}"은(는) 사용할 수 없는 이름입니다.'
        else:
            # DB에 저장
            Guest.objects.create(name=name_input)
            name = name_input

    guests = Guest.objects.order_by('-created_at')

    context = {
        'name': name,
        'error': error,
        'guests': guests
    }
    return render(request, 'myapp/hello_form.html', context)
