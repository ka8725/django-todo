from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
  url(r'^$', views.today, name='today'),
  url(r'^future$', views.future, name='future'),
  url(r'^fixed$', views.fixed, name='fixed'),
)