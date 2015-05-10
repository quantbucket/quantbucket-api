from analysis.models import Analysis, AnalysisVisualization
from rest_framework import serializers

class AnalysisSerializer(serializers.ModelSerializer):
	output = serializers.CharField(required=False)

    	class Meta:
        	model = Analysis
        	fields = ('id', 'dataset', 'algorithm', 'schema', 'output', 'created_at')

class AnalysisVisualizationSerializer(serializers.ModelSerializer):

    	class Meta:
        	model = AnalysisVisualization
        	fields = ('id', 'analysis', 'visualization', 'image', 'created_at')        	