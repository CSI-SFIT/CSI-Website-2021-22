from django.contrib import admin
from .models import Event, Images, PreviousEvent, PreviousEventImages
# Register your models here.
class EventAdmin(admin.ModelAdmin):
	model = Event
	fields = ('title', 'date', 'content', 'registrationLink', 'url')
	prepopulated_fields = {"url": ("title",)}


class PreviousEventAdmin(admin.ModelAdmin):
	model = Event
	fields = ('title', 'date', 'content', 'url')
	prepopulated_fields = {"url": ("title",)}

admin.site.register(Event, EventAdmin)
admin.site.register(Images)
admin.site.register(PreviousEvent, PreviousEventAdmin)
admin.site.register(PreviousEventImages)
