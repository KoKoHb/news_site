from django.urls import path
from .views import HomePageListView

urlpatterns = [
    path('', HomePageListView.as_view(), name='home'),

]
