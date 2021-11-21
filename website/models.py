from djongo import models
import uuid
import os

# Create your models here.

class Event(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	url = models.CharField(max_length=200, unique=True, verbose_name="URL (auto generated. Don't touch)")
	createdTime = models.DateTimeField(auto_now_add=True)
	updatedTime = models.DateTimeField(auto_now=True)
	title = models.CharField(max_length=100, null=True,verbose_name="Title")
	content = models.TextField(null=True,verbose_name="Content")
	registrationLink = models.CharField(max_length=200, null=True,verbose_name="Registration Link")
	
	def __str__(self):
		return(self.title)

def path_and_rename(instance, filename):
	upload_to = 'website/static/website/images/event_images/'
	filename=instance.event.title+str(len(Images.objects.filter(event=instance.event)))+'.jpg'
	return os.path.join(upload_to, filename)

class Images(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	event = models.ForeignKey(Event, default=None, on_delete=models.CASCADE, related_name="images")
	image = models.ImageField(upload_to=path_and_rename,
							verbose_name='image')
							
	def __str__(self):
		return(self.image.path.split('\\')[-1])
