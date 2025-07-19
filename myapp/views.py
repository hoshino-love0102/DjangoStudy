from django.shortcuts import render

def hello_form(request):
    name = ''
    error = ''

    if request.method == 'POST':
        name_input = request.POST.get('name', '').strip()

        # 유효성 검사
        if not name_input:
            error = '이름을 입력해주세요.'
        elif name_input.lower() in ['admin', 'root', 'badword']:
            error = f'"{name_input}"은(는) 사용할 수 없는 이름입니다.'
        else:
            name = name_input  # 유효할 때 출력

    context = {
        'name': name,
        'error': error
    }
    return render(request, 'myapp/hello_form.html', context)
