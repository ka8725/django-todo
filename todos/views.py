from django.shortcuts import render, redirect
from todos.models import Todo
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


def fix(req):
  todo_ids = req.POST.getlist('todo_ids')
  for todo in Todo.objects.filter(id__in=todo_ids):
    todo.fix()
  return redirect(_back_path(req))


def remove(req):
  todo_ids = req.POST.getlist('todo_ids')
  for todo in Todo.objects.filter(id__in=todo_ids):
    print todo
    todo.delete()
  return redirect(_back_path(req))


def _back_path(req):
  return req.META.get('HTTP_REFERER')
