from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin

from techwebprj.forms import CreaUtente, CreaUtenteEditore

def chitarrorchestra_home(request):
    return render(request, template_name="home.html")

class UserCreateView(CreateView):
    form_class = CreaUtente
    template_name = "user_create.html"
    success_url = reverse_lazy("login")

class BiblioCreateView(PermissionRequiredMixin, UserCreateView):
    permission_required = "is_staff"
    form_class = CreaUtenteEditore
    
