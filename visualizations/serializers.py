from visualizations.models import Visualization
from visualizations.models import VisualizationMapping
from rest_framework import serializers

class VisualizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Visualization
        fields = ('id', 'name', 'developer', 'algorithms', 'created_at')

class VisualizationMappingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VisualizationMapping
        fields = ('id', 'visualization', 'algorithm', 'visualization_field', 'algorithm_field')