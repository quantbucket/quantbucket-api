from algorithms.models import Algorithm
from rest_framework import serializers

class AlgorithmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Algorithm
        fields = ('id', 'name', 'developer', 'version', 'description', 'image', 'repository', 'created_at')