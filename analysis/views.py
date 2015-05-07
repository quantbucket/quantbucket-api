from django.http import HttpResponse
from algorithms.models import Algorithm
from datasets.models import Dataset
from visualizations.models import Visualization
from analysis.models import Analysis
from rest_framework import viewsets
from analysis.serializers import AnalysisSerializer
import json

class AnalysisViewSet(viewsets.ModelViewSet):
    	queryset = Analysis.objects.all()
    	serializer_class = AnalysisSerializer

	def perform_create(self, serializer):
		schema = self.request.data['schema']
		dataset = Dataset.objects.get(pk=self.request.data['dataset'])
		algorithm = Algorithm.objects.get(pk=self.request.data['algorithm'])
		instance = algorithm.load()
		response = instance(dataset.content(),schema).output
		serializer.save(dataset=dataset,algorithm=algorithm,schema=schema,output=str(response))