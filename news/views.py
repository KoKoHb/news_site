from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Category


class HomePageListView(ListView):
    template_name = 'news/home.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(is_published=True).select_related('category')


class NewsByCategoryListView(ListView):
    template_name = 'news/news_by_category.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category', 'author')


class NewsDetailView(DetailView):
    template_name = 'news/news_detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        return Post.objects.get(pk=self.kwargs['pk'], is_published=True)



