from visualizations.models import Visualization
from visualizations.models import VisualizationMapping
from rest_framework import viewsets
from visualizations.serializers import VisualizationSerializer
from visualizations.serializers import VisualizationMappingSerializer
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import detail_route

class VisualizationViewSet(viewsets.ModelViewSet):
    queryset = Visualization.objects.all()
    serializer_class = VisualizationSerializer

    @detail_route(methods=['get'])
    def mappings(self, request, pk=None):
    	algorithm_id = self.request.QUERY_PARAMS.get('algorithm_id', None)
    	viz = self.get_object()
    	mappings = viz.algorithm_mappings(algorithm_id)
    	serializer = VisualizationMappingSerializer(mappings, many=True)
    	return Response(serializer.data)

class VisualizationMappingViewSet(viewsets.ModelViewSet):
    queryset = VisualizationMapping.objects.all()
    serializer_class = VisualizationMappingSerializer