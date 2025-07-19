from django.shortcuts import render

def hello(request):
    fruits = ['사과', '바나나', '딸기']
    context = {
        'name': '우진',
        'fruits': fruits
    }
    return render(request, 'myapp/hello.html', context)