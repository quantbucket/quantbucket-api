from algorithms.models import Algorithm
from rest_framework import viewsets
from algorithms.serializers import AlgorithmSerializer
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import detail_route

class AlgorithmViewSet(viewsets.ModelViewSet):
    queryset = Algorithm.objects.all()
    serializer_class = AlgorithmSerializer

    @detail_route(methods=['get'])
    def schema(self, request, pk=None):
    	algorithm = self.get_object()
    	return Response(algorithm.schema())