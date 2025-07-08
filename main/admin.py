from django.contrib import admin
from .models import User, Work, Collection, CollectionWork, FeedbackForm

# Register your models here.
admin.site.register(User)
admin.site.register(Work)
admin.site.register(Collection)
admin.site.register(CollectionWork)
admin.site.register(FeedbackForm)
