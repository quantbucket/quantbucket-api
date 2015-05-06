from algorithms.models import Algorithm
from rest_framework import serializers

class AlgorithmSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Algorithm
        fields = ('id', 'name', 'developer', 'version', 'description', 'created_at')