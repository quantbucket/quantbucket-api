from django.db import models
import users
import csv
from StringIO import StringIO

def upload_path_handler(instance, filename):
    return "datasets/user_{id}/{file}".format(id=instance.user.id, file=filename)

class Dataset(models.Model):
	name = models.CharField(max_length=255)
	user = models.ForeignKey(users.models.User)
	data = models.FileField(upload_to=upload_path_handler)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table = 'datasets'

	def content(self):
		self.data.open()
		data = list(csv.DictReader(StringIO(self.data.read()),delimiter=','))
		return data