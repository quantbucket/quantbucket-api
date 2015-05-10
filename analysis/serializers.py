from analysis.models import Analysis, AnalysisVisualization
from rest_framework import serializers

class AnalysisVisualizationSerializer(serializers.HyperlinkedModelSerializer):

    	class Meta:
        	model = AnalysisVisualization
        	fields = ('id', 'visualization', 'image', 'created_at')

class AnalysisSerializer(serializers.HyperlinkedModelSerializer):
	output = serializers.CharField(required=False)
	visualizations = AnalysisVisualizationSerializer(many=True, read_only=True)

    	class Meta:
        	model = Analysis
        	fields = ('id', 'dataset', 'algorithm', 'schema', 'output', 'visualizations', 'created_at')