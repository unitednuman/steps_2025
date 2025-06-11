
from django.contrib import admin
from django.urls import path, include
from .views import ArticlesListView, ArticlesUpdateView

urlpatterns = [
    path('articles/', ArticlesListView.as_view(), name='articles-list'),
    path('articles/<int:pk>', ArticlesUpdateView.as_view()),
]
