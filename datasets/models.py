from django.db import models
import users
import csv
from StringIO import StringIO

class Dataset(models.Model):
	name = models.CharField(max_length=255)
	user = models.ForeignKey(users.models.User)
	data = models.FileField(upload_to=lambda instance, filename: 'datasets/{0}/{1}'.format(instance.user.id, filename))	
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table = 'datasets'

	def content(self):
		self.data.open()
		data = list(csv.DictReader(StringIO(self.data.read()),delimiter=','))
		return data