from django.contrib import admin
from .models import Queue, QueueEntry

# Register your models here.


admin.site.register(Queue)
admin.site.register(QueueEntry)
