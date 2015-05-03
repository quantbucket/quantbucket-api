from django.db import models
import users
import sys

class Algorithm(models.Model):
	name = models.CharField(max_length=255)
	developer = models.ForeignKey(users.models.User)
	module = models.CharField(max_length=255)
	version = models.CharField(max_length=255)
	description = models.TextField()

	def load(self):
		sys.path.append('algorithms/quantbucket-repo/modules/'+self.name)
		module = __import__('app')
		cls = getattr(module,'Application')
		return cls