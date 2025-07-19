from django.shortcuts import render

def hello(request):
    fruits = ['사과', '바나나', '딸기', '포도', '수박']
    context = {
        'name': '우진',
        'message': '과일 리스트입니다:',
        'fruits': fruits
    }
    return render(request, 'myapp/hello.html', context)