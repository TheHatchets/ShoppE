from django.shortcuts import render
from django.urls import reverse_lazy
from . import forms
from django.views.generic import CreateView
# Create your views here.
#reverse_lazy helps with when someone is logged in or logged out
#it helps tell where they should actually go.
#check the docs

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    #This is what controls what page they go to upon signing up
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'