from django.shortcuts import render

def hello(request):
    context = {
        'name': 'LWJ',
        'message': '장고 템플릿 변수 넘기기 성공!'
    }
    return render(request, 'myapp/hello.html', context)
