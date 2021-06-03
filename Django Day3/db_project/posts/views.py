from django.db.models.base import Model
from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


class HomePageView(ListView):
    model = Post
    template_name = 'Home.html'
    context_object_name = 'all_posts_list'