from django.db import models
import users

class Dataset(models.Model):
	name = models.CharField(max_length=255)
	user = models.ForeignKey(users.models.User)
	data = models.FileField()
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table = 'datasets'

	def content(self):
		docs = [
			{'name':'pepe','value':1},
			{'name':'cacho','value':3},
			{'name':'juan','value':5},
			{'name':'marcos','value':9}
		]
		return docs