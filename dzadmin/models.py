from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Message(models.Model):
	fullname = models.CharField(max_length=50)
	email = models.EmailField(null=False, blank=False)
	phoneno = models.IntegerField()
	msg = models.TextField()
	subject = models.CharField(max_length=100)
