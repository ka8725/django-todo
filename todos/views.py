from django.shortcuts import render
from models import Todo
from datetime import date

def today(req):
  todos = Todo.objects.filter(date__lte=date.today(), status=Todo.NEW)
  return render(req, 'todos/today.html', {'todos': todos})


def future(req):
  todos = Todo.objects.filter(date__gt=date.today(), status=Todo.NEW)
  return render(req, 'todos/future.html', {'todos': todos})


def fixed(req):
  todos = Todo.objects.filter(status=Todo.FIXED)
  return render(req, 'todos/fixed.html', {'todos': todos})
