from django.db import models
from django.contrib.auth.models import User, AnonymousUser

# Create your models here.
class Seed(models.Model):
     user = models.ForeignKey(User)
     seed_type = models.CharField(max_length=150, blank=True)
     crop_type = models.CharField(max_length=150, blank=True)
     seed_variety = models.CharField(max_length=150, blank=True)
     seed_description =models.TextField(blank=True)
     enough_to_share = models.BooleanField(default=False)
     year = models.CharField(max_length=150, blank=True)
     origin = models.CharField(max_length=150, blank=True)

     archived = models.BooleanField(default=False, blank=False)

     def __unicode__(self):
         return self.user.username + "\'s " + self.seed_type 

     def __str__(self):
         return self.user.username + "\'s " + self.seed_type 


class Event(models.Model):
	name = models.CharField(max_length=150, blank=True)
	date = models.DateField()
	show_on_seed_edit = models.BooleanField(default=True)

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name

class SeedAtEvent(models.Model):
	seed = models.ForeignKey(Seed)
	event = models.ForeignKey(Event)

	def __unicode__(self):
		return self.seed.seed_type + " at " + self.event.name

	def __str__(self):
		return self.seed.seed_type + " at " + self.event.name
