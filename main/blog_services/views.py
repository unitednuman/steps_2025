from django.shortcuts import render
from .models import Articles
from .serializer import ArticlesSerializer
from rest_framework import generics

# Create your views here.

class ArticlesListView(generics.ListCreateAPIView):
    serializer_class = ArticlesSerializer
    queryset = Articles.objects.all()



class ArticlesUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArticlesSerializer
    queryset = Articles.objects.all()


