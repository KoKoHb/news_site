from django.shortcuts import render
from django.views.generic import ListView
from .models import Post, Category


class HomePageListView(ListView):
    template_name = 'news/home.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(is_published=True).select_related('category')


