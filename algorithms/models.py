from django.db import models
import users
import sys
import json

def upload_path_handler(instance, filename):
	return "algorithms/{id}/{file}".format(id=instance.name, file=filename)

class Algorithm(models.Model):
	name = models.CharField(max_length=255)
	developer = models.ForeignKey(users.models.User)
	version = models.CharField(max_length=255)
	description = models.TextField()
	image = models.ImageField(upload_to=upload_path_handler, null=True)
	repository = models.CharField(max_length=255, null=True)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table = 'algorithms'

	def load(self):
		#Need to refactor this with python packages
		sys.path.append('algorithms/quantbucket-repo/')
		sys.path.append('algorithms/quantbucket-repo/algorithms/'+self.name)
		module = __import__(self.name)
		cls = getattr(module,'Application')
		return cls

	def schema(self):
		#Need to refactor this with python packages		
		sys.path.append('algorithms/quantbucket-repo/'+self.name)
		json_schema = open('algorithms/quantbucket-repo/algorithms/'+self.name+'/schema.json','r')
		return json.loads(json_schema.read())