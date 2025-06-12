from django.shortcuts import render
from .models import Articles, Reporter
from .serializer import ArticlesSerializer , ReporterSerializer
from rest_framework import generics

# Create your views here.

class ArticlesListView(generics.ListCreateAPIView):
    serializer_class = ArticlesSerializer
    queryset = Articles.objects.all()



class ArticlesUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArticlesSerializer
    queryset = Articles.objects.all()



class ReporterListView(generics.ListCreateAPIView):
    serializer_class = ReporterSerializer
    queryset = Reporter.objects.all()



class ReporterUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReporterSerializer
    queryset = Reporter.objects.all()



