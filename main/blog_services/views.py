from django.shortcuts import render
from .models import Articles, Reporter , Publisher
from .serializer import ArticlesSerializer , ReporterSerializer , PublisherSerializer
from rest_framework import generics
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

# Create your views here.

class ArticlesListView(generics.ListCreateAPIView):
    serializer_class = ArticlesSerializer
    queryset = Articles.objects.all()

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(name='title',
                              in_ = openapi.IN_QUERY,description='Article Tile filter',
                              type = openapi.TYPE_STRING),
        ]
    )
    def get(self, request, *args, **kwargs):
        filters = {}
        title = request.GET.get('title')
        if title:
            filters.update({'title': title})
        if filters:
            queryset = self.queryset.filter(**filters)
        else:
            queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)

class ArticlesUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArticlesSerializer
    queryset = Articles.objects.all()



class ReporterListView(generics.ListCreateAPIView):
    serializer_class = ReporterSerializer
    queryset = Reporter.objects.all()



class ReporterUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReporterSerializer
    queryset = Reporter.objects.all()

class PublisherListView(generics.ListCreateAPIView):
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()
class PublisherUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()