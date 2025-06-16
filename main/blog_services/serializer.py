from .models import Articles , Reporter , Publisher
from rest_framework import serializers

class ReporterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reporter
        fields = '__all__'
        # fields = ('title', 'content')
        # read_only_fields = ('id',)
        # write_only_fields = ('title',)

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'

class ArticlesSerializer(serializers.ModelSerializer):
    # reporter = ReporterSerializer(read_only=True)
    # publisher = PublisherSerializer(read_only=True, many=True)
    class Meta:
        model = Articles
        fields = '__all__'

    def to_representation(self, instance):
        data = super(ArticlesSerializer,self).to_representation(instance)
        if reporter := instance.reporter:
            serialized = ReporterSerializer(reporter).data
            data.update({'reporter': serialized})

        return data
