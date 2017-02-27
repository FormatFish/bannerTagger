from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Banner(models.Model):
	#id = models.AutoField()
	name = models.CharField(max_length = 100)
	width = models.IntegerField()
	height = models.IntegerField()
	ratio = models.FloatField()
	category = models.IntegerField()
	imgCount = models.IntegerField()
	imgElement = models.TextField()
	textCount = models.IntegerField()
	textElement = models.TextField()
	textAlignment = models.IntegerField()
	dominantColor = models.CharField(max_length = 255)
	palette =models.CharField(max_length = 255)
	backgroundColor = models.CharField(max_length = 100)
	textColor = models.CharField(max_length = 100)
	backgroundCategory = models.IntegerField()