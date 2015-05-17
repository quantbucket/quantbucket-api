from datasets.models import Dataset
from rest_framework import serializers

class DatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dataset
        fields = ('id', 'name', 'user', 'data', 'created_at')