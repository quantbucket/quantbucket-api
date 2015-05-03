from django.http import HttpResponse
import algorithms
import datasets
import visualizations
import json

def run(request):
	dataset = datasets.models.Dataset.objects.get(pk=request.GET['dataset']).content()
	algorithm = algorithms.models.Algorithm.objects.get(pk=request.GET['algorithm']).load()
	response = algorithm(dataset).output
	return HttpResponse(json.dumps(response))