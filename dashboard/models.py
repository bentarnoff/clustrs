from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Clustr(models.Model):

	name = models.CharField(max_length=100)

	def __unicode__(self):
		return unicode(self.name)

class Nugget(models.Model):

	clustr = models.ForeignKey('Clustr')

	text_or_nah = models.NullBooleanField(default=None, blank=True, null=True)

	title = models.CharField(max_length=100)
	author = models.CharField(max_length=100, default=None, blank=True, null=True)
	source = models.CharField(max_length=100, default=None, blank=True, null=True)
	date = models.CharField(max_length=100)

	thumbnail_text = models.TextField(default=None, blank=True, null=True)
	thumbnail_url = models.CharField(default=None, blank=True, null=True, max_length=500)
	comment = models.TextField()
	read_time = models.IntegerField()
	contributor = models.CharField(max_length=100)
	votes = models.IntegerField()

	link_url = models.URLField(default=None, blank=True, null=True)


	def __unicode__(self):
		return u"{0}, {1}, {2}, {3}".format(self.title, self.author, self.source, self.date)

	class Meta:
		ordering = ['-votes']

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	active_clustrs = models.ManyToManyField(Clustr, default=None, blank=True)
	queue = models.ManyToManyField(Nugget, related_name='nuggets_in_queue', default=None, blank=True)
	contributions = models.ManyToManyField(Nugget, related_name='contributed_nuggets', default=None, blank=True)
   	cred = models.IntegerField(default=None, blank=True, null=True)

   	def __unicode__(self):
   		return u"{0}, {1}, {2}, {3}, {4}".format(self.user, self.active_clustrs, self.queue, self.contributions, self.cred)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
    