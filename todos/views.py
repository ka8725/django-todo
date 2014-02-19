from django.shortcuts import render
from models import Todo
from datetime import date

def today(req):
  todos = Todo.objects.filter(date__lte=date.today())
  return render(req, 'todos/today.html', {'todos': todos})


def feature(req):
  todos = Todo.objects.filter(date__gt=date.today())
  return render(req, 'todos/feature.html', {'todos': todos})


def fixed(req):
  return render(req, 'todos/fixed.html')
