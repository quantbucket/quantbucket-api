from django.db import models
import users
import sys

class Algorithm(models.Model):
	name = models.CharField(max_length=255)
	developer = models.ForeignKey(users.models.User)
	version = models.CharField(max_length=255)
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table = 'algorithms'

	def load(self):
		sys.path.append('algorithms/quantbucket-repo/modules/'+self.name)
		module = __import__('app')
		cls = getattr(module,'Application')
		return cls