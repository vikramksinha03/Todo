from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Task

# Create your views here.

def add_task(request):
  task = request.POST['task']
  Task.objects.create(task=task)
  return redirect('home')