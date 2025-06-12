from .models import Articles , Reporter
from rest_framework import serializers



class ArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = '__all__'
        # fields = ('title', 'content')
        # read_only_fields = ('id',)
        # write_only_fields = ('title',)


class ReporterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporter
        fields = '__all__'
        # fields = ('title', 'content')
        # read_only_fields = ('id',)
        # write_only_fields = ('title',)