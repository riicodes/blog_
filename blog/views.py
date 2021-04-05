from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post


class PostList(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = "all_posts"


class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'


class PostCreate(CreateView):
    model = Post
    fields = ['title', 'body', 'author']
    template_name = 'post_create.html'


class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'body']
    template_name = 'post_edit.html'


class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
