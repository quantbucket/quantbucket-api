from analysis.models import Analysis
from rest_framework import serializers

class AnalysisSerializer(serializers.ModelSerializer):
	output = serializers.CharField(required=False)
    	class Meta:
        	model = Analysis
        	fields = ('id', 'dataset', 'algorithm', 'output', 'created_at')
