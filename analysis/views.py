from django.http import HttpResponse
from algorithms.models import Algorithm
from datasets.models import Dataset
from visualizations.models import Visualization
from analysis.models import Analysis, AnalysisVisualization
from rest_framework import viewsets
from analysis.serializers import AnalysisSerializer,AnalysisVisualizationSerializer
import json
from django.core.files import File
from django.core.files.base import ContentFile
from rest_framework.decorators import detail_route
from rest_framework.response import Response


class AnalysisViewSet(viewsets.ModelViewSet):
    	queryset = Analysis.objects.all()
    	serializer_class = AnalysisSerializer

	def perform_create(self, serializer):
		schema = self.request.data['schema']
		dataset = Dataset.objects.get(pk=self.request.data['dataset'])
		algorithm = Algorithm.objects.get(pk=self.request.data['algorithm'])
		instance = algorithm.load()
		response = instance(dataset.content(),schema).output
		new_analysis = serializer.save(dataset=dataset,algorithm=algorithm,schema=json.dumps(schema),output=json.dumps(response))
		self.plot(new_analysis)

	def plot(self,analysis):
		vizs = analysis.algorithm.visualization_set.all()
		for v in vizs:
			viz_backend = v.load()
			viz_schema = v.schema_mapper(analysis)
			response = viz_backend(analysis.dataset.content(),viz_schema).output
			analysis_viz =  AnalysisVisualization(analysis=analysis,visualization=v)
			analysis_viz.image.save(v.name,ContentFile(response.getvalue()))
			analysis_viz.save()