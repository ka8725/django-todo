from django.shortcuts import render


def today(req):
  return render(req, 'todos/today.html')


def feature(req):
  return render(req, 'todos/feature.html')


def fixed(req):
  return render(req, 'todos/fixed.html')
