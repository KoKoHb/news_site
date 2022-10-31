from django.urls import path
from .views import HomePageListView, NewsByCategoryListView, NewsDetailView

urlpatterns = [
    path('', HomePageListView.as_view(), name='home'),
    path('categories/<int:category_id>/', NewsByCategoryListView.as_view(), name='news_by_category'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
]
