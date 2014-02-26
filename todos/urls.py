from django.conf.urls import patterns, url
from todos.views import TodoView

import views

urlpatterns = patterns('',
  url(r'^$', views.today, name='today'),
  url(r'^future$', views.future, name='future'),
  url(r'^fixed$', views.fixed, name='fixed'),
  url(r'^fix$', views.fix, name='fix'),
  url(r'^remove$', views.remove, name='remove'),
  url(r'^new$', TodoView.as_view(), name='new'),
)
