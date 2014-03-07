from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from required import required
from django.contrib import admin

import views

admin.autodiscover()

urlpatterns = patterns('',
  url(r'^admin/', include(admin.site.urls)),
  url(r'^accounts/', include('django.contrib.auth.urls')),
  url(r'^accounts/', include('registration.backends.default.urls')),
)

urlpatterns += required(
  login_required,
  patterns('',
    url(r'^todos/', include('todos.urls', namespace='todos')),
  )
)
