from __future__ import unicode_literals

from django.db import models

class around_locations(models.Model):
	name = models.CharField(max_length=50)
	latitude = models.CharField(max_length=50)
	longitude = models.CharField(max_length=50)

	def __unicode__(self):
	    return u'%s' % (self.name)

class locate(models.Model):
	name = models.CharField(max_length=50, null=True, blank=True)
	latitude = models.CharField(max_length=50)
	longitude = models.CharField(max_length=50)
	around = models.ManyToManyField(around_locations, blank=True)
