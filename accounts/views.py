from django.shortcuts import render,redirect
from django.contrib.auth import login
from django.views  import View
from accounts.forms import RegistrationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy


class RegisterView(CreateView):
    form_class = RegistrationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("accounts:login")