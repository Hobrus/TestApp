from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def hello(request):
    return HttpResponse("Hello, world!")


def site(request):
    items = [
        {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
        {"id": 2, "name": "Куртка кожаная", "quantity": 2},
        {"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
        {"id": 7, "name": "Картофель фри", "quantity": 0},
        {"id": 8, "name": "Кепка", "quantity": 124},
    ]
    context = {'goods': items}
    return render(request, 'main.html', context)
