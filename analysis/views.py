from django.http import HttpResponse
from algorithms.models import Algorithm
from datasets.models import Dataset
from visualizations.models import Visualization
from analysis.models import Analysis
import json

def run(request):
	dataset = Dataset.objects.get(pk=request.GET['dataset'])
	algorithm = Algorithm.objects.get(pk=request.GET['algorithm'])
	instance = algorithm.load()
	response = instance(dataset.content()).output
	analysis = Analysis(dataset=dataset,algorithm=algorithm,output=response)
	analysis.save()
	response = {
		'algorithm' : algorithm.name,
		'dataset' : dataset.name,
		'result' : response,
		'status' : 200
	}
	return HttpResponse(json.dumps(response))