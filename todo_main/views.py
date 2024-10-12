from django.http import HttpResponse
from django.shortcuts import render
from todos.models import Task

def home(request):
  tasks = Task.objects.filter(is_completed = False).order_by('-updated_at')
  completed_task = Task.objects.filter(is_completed=True)
  context = {
    'tasks': tasks,
    'completed_task': completed_task
  }
  return render(request, 'home.html', context)