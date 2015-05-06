from datasets.models import Dataset
from rest_framework import viewsets
from datasets.serializers import DatasetSerializer
from django.http import HttpResponse
from django.core.files import File

class DatasetViewSet(viewsets.ModelViewSet):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer