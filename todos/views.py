from datetime import date
from todos.models import Todo
from django.db import transaction
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.decorators.csrf import csrf_protect
from django.core.urlresolvers import reverse


class TodoView(CreateView):
  model = Todo
  fields = ('name', 'date')

  def get_success_url(self):
    return reverse('todos:today')

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
@transaction.commit_on_success
def fix(req):
  return _process_todos(req, lambda x: x.fix())


@csrf_protect
@transaction.commit_on_success
def remove(req):
  return _process_todos(req, lambda x: x.delete())


def _process_todos(req, command):
 todo_ids = req.POST.getlist('todo_ids')
 map(command, Todo.objects.filter(id__in=todo_ids, user=req.user))
 return redirect(req.META.get('HTTP_REFERER'))
