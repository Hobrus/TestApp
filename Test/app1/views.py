from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt

from .models import Task


# Create your views here.
@csrf_exempt
def site(request):
    if request.method == 'POST':
        auth.logout(request)
    context = {}
    result = []
    queryset = Task.objects.all()
    for el in queryset:
        answer = f'{el.id}) {el.name}: {el.time}'
        result.append(answer)
    context['tasks'] = result
    return render(request, 'main.html', context)


@csrf_exempt
@login_required(login_url=reverse_lazy('login'))
def addtask(request):
    if request.method == 'POST':
        task_id = request.POST.get('id')
        task_name = request.POST.get('name')
        task_time = request.POST.get('time')
        task = Task(id=task_id, name=task_name, time=task_time)
        task.save()
        return redirect('home')  # Редирект на главную страницу после добавления задачи
    return render(request, 'addtask.html')


@csrf_exempt
@login_required(login_url=reverse_lazy('login'))
def removetask(request):
    if request.method == 'POST':
        task_id = request.POST.get('id')
        el = Task.objects.filter(id=task_id).first()
        el.delete()
        return redirect('home')  # Редирект на главную страницу после удаления задачи
    context = {}
    result = []
    queryset = Task.objects.all()
    for el in queryset:
        answer = f'{el.id}) {el.name}: {el.time}'
        result.append(answer)
    context['tasks'] = result
    return render(request, 'removetask.html', context)


@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            print('User not found')
            pass

    return render(request, 'registration/login.html')


@csrf_exempt
def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('login'))  # Используйте HttpResponseRedirect для перенаправления на страницу логина после успешной регистрации
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'registration.html', context)


