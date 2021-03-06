from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import SelectRelatedMixin
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView
from django.urls import reverse_lazy

from . import models
from . import forms

from django.contrib.auth import get_user_model
User=get_user_model



# Create your views here.

class PostList(SelectRelatedMixin,listView):
    model=Post
    select_related=('user','group')

class UserPosts(ListView):
    model=Post
    template_name='posts/user_post_list.html'

    def get_queryset(self):
        try:
            self.post.user=User.objects.prefetch_related('post').get(username__iexact=self.keargs.get('usrename'))
        except User.DoestNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['post_user']=self.post_user
        return context

class PostDetail(SelectRelatedMixin,DetailView):
    model=Post
    select_related=('user','group')

    def get_queryset(self):
        queryset=super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get('username'))

class CreatePost(LoginRequiredMixin,SelectRelatedMixin,CreateView):
    fields=('group','message')
    model=Post

    def form_valid(self,form):
        self.object=form.save(commit=False)
        self.object.user=self.request.user
        self.object.save()
        return super().form_valid(form)

class DeletePost(LoginRequiredMixin,SelectRelatedMixin,DeleteView):
    model=Post
    success_url=reverse_lazy('post:all')
    select_related=('user','group')

    def get_queryset(self):
        queryset=super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self,**args,**kwargs):
        message.success(self.request,"Post Deleted")
        return super().delete(*args,**kwargs)
