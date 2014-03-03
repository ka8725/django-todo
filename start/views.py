from django.contrib.auth import logout
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

def app_logout(request):
  logout(request)
  return redirect(reverse('login'))
