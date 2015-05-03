from django.db import models
import users

# Create your models here.
class Dataset(models.Model):
	name = models.CharField(max_length=255)
	user = models.ForeignKey(users.models.User)
	data = models.FileField()

	def content(self):
		docs = [
			{'name':'pepe','value':1},
			{'name':'cacho','value':3},
			{'name':'juan','value':5},
			{'name':'marcos','value':9}
		]
		return docs