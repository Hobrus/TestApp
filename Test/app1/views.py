from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def hello(request):
    return HttpResponse("Hello, world!")


def hello2(request):
    name = "Иванов И.П."
    return HttpResponse(f'''
<h1>"Изучаем django"</h1>
<strong>Автор</strong>: <i>{name}</i>
''')
