from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from django.contrib.auth.models import AbstractUser

class locate(models.Model):
	name = models.CharField(max_length=50, null=True, blank=True)
	google_map_name = models.CharField(max_length=100, blank=True, null=True)
	latitude = models.CharField(max_length=50)
	longitude = models.CharField(max_length=50)

	class Meta:
	    unique_together = ('latitude','longitude')

class AppUser(AbstractUser):
	type_choices = (
		('Manager', 'Manager'),
		('User', 'User'),
		('ServiceOwner', 'Service Owner')
	)
	user_type = models.CharField(max_length=500, choices=type_choices)

	def save(self, *args, **kwargs):
		if self.is_superuser:
			self.user_type = 'Manager'
		super(AppUser, self).save(*args, **kwargs)

@receiver(pre_save, sender=AppUser)
def my_callback(sender, instance, *args, **kwargs):
    pass_filter = AppUser.objects.filter(username = instance.username)
    if pass_filter:
        if pass_filter[0].password != instance.password:
            instance.set_password(instance.password)
        else:
            pass
    else:
        if instance.is_superuser:
            pass
        else:
            instance.set_password(instance.password)