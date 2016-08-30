from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Show(models.Model):
	title = models.CharField(max_length=128)
	episodes = models.IntegerField(default=0)

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

class User(models.Model):
	email = models.EmailField(max_length=254, unique=True)
	name = models.CharField(max_length=128)
	shows = models.ManyToManyField(Show)
	# this is for python 2, for python 3 use __str__
	def __unicode__(self):		
		return self.email

