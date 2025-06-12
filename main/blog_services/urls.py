
from django.contrib import admin
from django.urls import path, include
from .views import ArticlesListView, ArticlesUpdateView , ReporterUpdateView , ReporterListView

urlpatterns = [
    path('articles/', ArticlesListView.as_view(), name='articles-list'),
    path('articles/<int:pk>', ArticlesUpdateView.as_view()),

    path('reporter/', ReporterListView.as_view(), name='reporter-list'),
    path('reporter/<int:pk>', ReporterUpdateView.as_view()),
]
