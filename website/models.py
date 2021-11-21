from djongo import models
import uuid

# Create your models here.


class Event(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	url = models.CharField(max_length=200, unique=True)
	createdTime = models.DateTimeField(auto_now_add=True)
	updatedTime = models.DateTimeField(auto_now=True)
	title = models.CharField(max_length=100, null=True)
	content = models.TextField(null=True)
	registrationLink = models.CharField(max_length=200, null=True)
	
	def __str__(self):
		return(self.title)

class Images(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	event = models.ForeignKey(Event, default=None, on_delete=models.CASCADE)
	image = models.ImageField(upload_to="website/static/website/images/event_images/",
							verbose_name='Image')

	def delete(self, *args, **kwargs):
		self.image.delete()
		super(Images, self).delete(*args, **kwargs)
