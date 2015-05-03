from django.db import models
import algorithms
import datasets

# Create your models here.
class Analysis(models.Model):
	dataset = models.ForeignKey(datasets.models.Dataset)
	algorithm = models.ForeignKey(algorithms.models.Algorithm)