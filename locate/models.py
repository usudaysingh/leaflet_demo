from __future__ import unicode_literals

from django.db import models

class locate(models.Model):
	name = models.CharField(max_length=50, null=True, blank=True)
	latitude = models.CharField(max_length=50)
	longitude = models.CharField(max_length=50)