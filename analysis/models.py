from django.db import models
import algorithms
import datasets
from visualizations.models import Visualization

def upload_path_handler(instance, filename):
    return "analysis/{analysis_id}/{visualization_name}.png".format(analysis_id=instance.analysis.id, visualization_name=instance.visualization.name)

class Analysis(models.Model):
	dataset = models.ForeignKey(datasets.models.Dataset)
	algorithm = models.ForeignKey(algorithms.models.Algorithm)
	schema = models.TextField()
	output = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table = 'analysis'

class AnalysisVisualization(models.Model):
	analysis = models.ForeignKey(Analysis, related_name='visualizations')
	visualization = models.ForeignKey(Visualization)
	image = models.FileField(upload_to=upload_path_handler)
	created_at = models.DateTimeField(auto_now_add=True)