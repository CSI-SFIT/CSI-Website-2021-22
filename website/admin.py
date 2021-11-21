from django.contrib import admin
from .models import Event,Images
# Register your models here.
class EventAdmin(admin.ModelAdmin):
	model = Event
	fields = ('title', 'content', 'registrationLink', 'url')
	prepopulated_fields = {"url": ("title",)}

admin.site.register(Event, EventAdmin)
admin.site.register(Images)
