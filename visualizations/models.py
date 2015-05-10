from django.db import models
import users
import analysis
import algorithms
import json
import sys

class Visualization(models.Model):
    	ARCHS = (
        	('frontend', 'frontend'),
        	('backend', 'backend'),
    	)
	name = models.CharField(max_length=255)
	arch = models.CharField(max_length=10,choices=ARCHS)
	developer = models.ForeignKey(users.models.User)
	version = models.CharField(max_length=255)
	algorithms = models.ManyToManyField(algorithms.models.Algorithm)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table = 'visualizations'

	def algorithm_mappings(self,algorithm_id):
		mappings = self.visualizationmapping_set.filter(algorithm=algorithm_id)
		return mappings

	def schema_mapper(self,analysis):
		mappings = self.visualizationmapping_set.filter(algorithm=analysis.algorithm)
		algorithm_schema = json.loads(analysis.schema)
		visualization_schema = dict()
		for m in mappings:
			visualization_schema[m.visualization_field] = algorithm_schema[m.algorithm_field]
		return visualization_schema


	def load(self):
		#Need to refactor this with python packages
		sys.path.append('algorithms/quantbucket-repo/')
		sys.path.append('algorithms/quantbucket-repo/visualizations/'+self.name)
		module = __import__('chart')
		cls = getattr(module,'Chart')
		return cls


class VisualizationMapping(models.Model):
	visualization = models.ForeignKey(Visualization)
	algorithm = models.ForeignKey(algorithms.models.Algorithm)
	visualization_field = models.CharField(max_length=255)
	algorithm_field = models.CharField(max_length=255)