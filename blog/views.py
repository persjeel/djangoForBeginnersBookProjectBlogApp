from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from .models import Post


# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(CreateView):
    # specified database model, Post
    model = Post
    template_name = 'post_new.html'
    # specified database fields to expose in form
    fields = ['title', 'author', 'body']
