from django.urls import path
from .views import HomePageListView, NewsByCategoryListView, NewsDetailView, register_user, login_user, logout_user, PostCreateView, Search

urlpatterns = [
    path('', HomePageListView.as_view(), name='home'),
    path('categories/<int:category_id>/', NewsByCategoryListView.as_view(), name='news_by_category'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('add_news/', PostCreateView.as_view(), name='add_post'),
    path('search/', Search.as_view(), name='search'),
]
