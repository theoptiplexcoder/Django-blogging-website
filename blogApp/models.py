from django.db import models
import datetime
# Create your models here.

class BlogPost(models.Model):
	title=models.CharField(max_length=100)
	body=models.TextField(max_length=1000)
	created=models.DateTimeField(auto_now_add=True)