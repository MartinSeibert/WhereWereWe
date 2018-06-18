from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

import tvdbsimple as tvdb
tvdb.KEYS.API_KEY = '491A6814F8241D30'

# Create your models here.

class Show(models.Model):
	tvdb_id = model.PositiveIntigerField()
	title = models.CharField(max_length=128)
	episodes = models.ManyToManyField(Episode)

	# a slug field replaces spaces in the title with hyphens so that we can create human readable urls
	slug = models.SlugField()

	# to create the slug on save, we need to customize the save method
	def save(self, *args, **kwargs):
		# Uncomment this if you don't want the slug to change every time the name changes
		# if self.id is None:
		# self.slug = slugify(self.name)

		self.slug = slugify(self.title)
		super(Show, self).save(*args, **kwargs)

	def __unicode__(self):
		return self.title

class UserProfile(models.Model):

	# links UserProfile to a User model instance (User is native to django)
	user = models.OneToOneField(User)
	shows = models.ManyToManyField(Show)
	picture = models.ImageField(upload_to='profile_images', blank=True)

	# this is for python 2, for python 3 use __str__
	def __unicode__(self):		
		return self.user.username