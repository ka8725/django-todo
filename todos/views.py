from django.shortcuts import render, redirect
from todos.models import Todo
from datetime import date
from django.views.generic.edit import CreateView
from django.views.decorators.csrf import csrf_protect


class TodoView(CreateView):
  model = Todo
  fields = ('name', 'date')

  # Figure out how to use here resolve() or reverse() function in this context
  success_url = '/todos/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super(TodoView, self).form_valid(form)


def today(req):
  todos = Todo.objects.filter(date__lte=date.today(), status=Todo.NEW, user=req.user)
  return render(req, 'todos/today.html', {'todos': todos})


def future(req):
  todos = Todo.objects.filter(date__gt=date.today(), status=Todo.NEW, user=req.user)
  return render(req, 'todos/future.html', {'todos': todos})


def fixed(req):
  todos = Todo.objects.filter(status=Todo.FIXED, user=req.user)
  return render(req, 'todos/fixed.html', {'todos': todos})


@csrf_protect
def fix(req):
  todo_ids = req.POST.getlist('todo_ids')
  for todo in Todo.objects.filter(id__in=todo_ids, user=req.user):
    todo.fix()
  return redirect(_back_path(req))

@csrf_protect
def remove(req):
  todo_ids = req.POST.getlist('todo_ids')
  for todo in Todo.objects.filter(id__in=todo_ids, user=req.user):
    todo.delete()
  return redirect(_back_path(req))


def _back_path(req):
  return req.META.get('HTTP_REFERER')
