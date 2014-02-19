from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
  url(r'^$', views.today, name='today'),
  url(r'^feature$', views.feature, name='feature'),
  url(r'^fixed$', views.fixed, name='fixed'),
)