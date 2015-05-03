from django.db import models
import algorithms
import datasets

class Analysis(models.Model):
	dataset = models.ForeignKey(datasets.models.Dataset)
	algorithm = models.ForeignKey(algorithms.models.Algorithm)
	output = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table = 'analysis'