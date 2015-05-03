from django.db import models
import users
import analysis
import algorithms

class Visualization(models.Model):
	name = models.CharField(max_length=255)
	developer = models.ForeignKey(users.models.User)
	code = models.TextField()
	version = models.CharField(max_length=255)
	algorithm = models.ManyToManyField(algorithms.models.Algorithm)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table = 'visualizations'	