from django.db import models
import users
import analysis

# Create your models here.
class Visualization(models.Model):
	name = models.CharField(max_length=255)
	developer = models.ForeignKey(users.models.User)
	code = models.TextField()
	version = models.CharField(max_length=255)

class Result(models.Model):
	analysis = models.ForeignKey(analysis.models.Analysis)
	output = models.TextField()
	visualization =  models.ManyToManyField(Visualization)