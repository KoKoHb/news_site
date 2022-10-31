from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView

from .forms import AddPostForm, UserRegister, UserLogin
from .models import Post, Category


class HomePageListView(ListView):
    template_name = 'news/home.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(is_published=True).select_related('category', 'author')


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


class PostCreateView(CreateView):
    form_class = AddPostForm
    template_name = "news/add_post.html"

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        messages.success(self.request, "Статья будет добавлена после проверки администратором")
        return redirect("home")


def register_user(request):
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        return render(request, template_name="news/register.html", context={"form": form})
    form = UserRegister()
    return render(request, template_name="news/register.html", context={"form": form})


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            return redirect('home')
    form = UserLogin()
    return render(request, 'news/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect("login")


class Search(ListView):
    model = Post
    template_name = "news/search_results.html"

    def get_queryset(self):
        query = self.request.GET.get("search_string")
        object_list = Post.objects.filter(
            Q(title__icontains=query) | Q(article__icontains=query)
        ).select_related('category', 'author')
        return object_list
