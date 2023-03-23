from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from django.shortcuts import redirect
from .models import Task
from django.contrib.auth.forms import UserCreationForm


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
@login_required
def addtask(request):
    if request.method == 'POST':
        task_id = request.POST.get('id')
        task_name = request.POST.get('name')
        task_time = request.POST.get('time')
        task = Task(id=task_id, name=task_name, time=task_time)
        task.save()
    return render(request, 'addtask.html')


@csrf_exempt
@login_required
def removetask(request):
    if request.method == 'POST':
        task_id = request.POST.get('id')
        el = Task.objects.filter(id=task_id).first()
        el.delete()
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

    return render(request, 'login.html')


@csrf_exempt
def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('username')
            user = auth.authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('home')
            else:
                print('User not found')
                pass
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'registration.html', context)
