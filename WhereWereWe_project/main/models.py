from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.

class Episode(models.Model):
	title = models.CharField(max_length=128)

	slug = models.SlugField()

	def save(self, *args, **kwargs):

		self.slug = slugify(self.title)
		super(Episode, self).save(*args, **kwargs)

		def __unicode(self):
			return self.title

class Show(models.Model):
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

	def __unicode(self):
		return self.title

class UserProfile(models.Model):

	# links UserProfile to a User model instance (User is native to django)
	user = models.OneToOneField(User)
	shows = models.ManyToManyField(Show)
	picture = models.ImageField(upload_to='profile_images', blank=True)

	# this is for python 2, for python 3 use __str__
	def __unicode__(self):		
		return self.user.username