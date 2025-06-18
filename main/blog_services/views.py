from django.db.models import Q
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated

from .models import Articles, Reporter , Publisher
from .serializer import ArticlesSerializer , ReporterSerializer , PublisherSerializer
from rest_framework import generics
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

# Create your views here.

class ArticlesListView(generics.ListCreateAPIView):
    serializer_class = ArticlesSerializer
    queryset = Articles.objects.all()
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(name='title',
                              in_ = openapi.IN_QUERY,description='Article Tile filter',
                              type = openapi.TYPE_STRING),
            openapi.Parameter(name='reporter_name',
                              in_=openapi.IN_QUERY, description='Search by reporter name',
                              type=openapi.TYPE_STRING),
            openapi.Parameter(name='publisher_ids',
                              in_=openapi.IN_QUERY, description='Search by publisher ids',
                              type=openapi.TYPE_ARRAY, items=openapi.Items(type = openapi.TYPE_INTEGER)),

        ]
    )
    def get(self, request, *args, **kwargs):
        # filters = {'user_id': request.user.id}
        filters = {}
        title = request.GET.get('title')
        reporter_name = request.GET.get('reporter_name')
        publisher_ids = request.GET.get('publisher_ids')
        if title:
            filters.update({'title__icontains': title})
        if reporter_name:
            filters.update({'reporter__first_name__icontains': reporter_name})


        if publisher_ids:
            # publisher_ids = publisher_ids.split(',')
            # ['1','2','3']
            # int_publisher_ids = []
            # for id in  publisher_ids:
            #     int_publisher_ids.append(int(id))
            filters.update({'publisher__id__in': [int(x) for x in publisher_ids.split(',')]})

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
    permission_classes = [IsAuthenticated]



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