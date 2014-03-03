from django.conf.urls import patterns, include, url

import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
  url(r'^admin/', include(admin.site.urls)),
  url(r'^todos/', include('todos.urls', namespace='todos')),
  url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
  url(r'^accounts/logout/$', views.app_logout, name='logout'),
)
