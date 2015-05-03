from django.db import models

# Create your models here.
class User(models.Model):
	email = models.EmailField()
	password = models.CharField(max_length=50)
	api_key = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		db_table = 'users'