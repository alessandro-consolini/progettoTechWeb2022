#nella app gestione

from django.shortcuts import render
#from django.urls import reverse_lazy
#from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
#from django.contrib.auth.mixins import PermissionRequiredMixin

def chitarrorchestra_home(request):
    return render(request, template_name="home.html")
