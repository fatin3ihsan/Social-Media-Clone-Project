from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.urls import reverse
from groups.model import Group,GroupMember
from django.views.generic import  CreateView,ListView,UpdateView,DeleteView,DetailView
# Create your views here.

class CreateGroup(LoginRequiredMixin,CreateView):
    fields=('name','description')
    model=Group

class SingleGroup(DetailView):
    model=Group

class GroupList(ListView):
    model=Group
