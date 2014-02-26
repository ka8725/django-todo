from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
  url(r'^$', views.today, name='today'),
  url(r'^future$', views.future, name='future'),
  url(r'^fixed$', views.fixed, name='fixed'),
  url(r'^fix$', views.fix, name='fix'),
  url(r'^remove$', views.remove, name='remove'),
  url(r'^new$', views.new, name='new'),
)