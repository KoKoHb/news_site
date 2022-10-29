from django.shortcuts import render
from django.views.generic import ListView
from .utils import CategoryMixin
from .models import Post, Category


class HomePageListView(CategoryMixin, ListView):
    model = Post
    template_name = 'news/home.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cats = self.get_category()
        return context | cats

