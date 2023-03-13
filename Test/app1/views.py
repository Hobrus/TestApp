from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Task


# Create your views here.
def site(request):
    context = {}
    result = []
    queryset = Task.objects.all()
    for el in queryset:
        answer = f'{el.id}) {el.name}: {el.time}'
        result.append(answer)
    context['tasks'] = result
    return render(request, 'main.html', context)


@csrf_exempt
def add_task(request):
    if request.method == 'POST':
        task_id = request.POST.get('id')
        task_name = request.POST.get('name')
        task_time = request.POST.get('time')
        task = Task(id=task_id, name=task_name, time=task_time)
        task.save()
    return render(request, 'add_task.html')

