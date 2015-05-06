from algorithms.models import Algorithm
from rest_framework import viewsets
from algorithms.serializers import AlgorithmSerializer
from django.http import HttpResponse

class AlgorithmViewSet(viewsets.ModelViewSet):
    queryset = Algorithm.objects.all()
    serializer_class = AlgorithmSerializer