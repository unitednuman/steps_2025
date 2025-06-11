from .models import Articles
from rest_framework import serializers



class ArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articles
        fields = '__all__'
        # fields = ('title', 'content')
        # read_only_fields = ('id',)
        # write_only_fields = ('title',)