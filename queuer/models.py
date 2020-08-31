# Imports from python
from uuid import uuid4

# Imports from django
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _

# Imports from foreign installed apps

# Imports from local apps

# Start of Models


class Queue(models.Model):
    class Meta:
        verbose_name = "Queue"
        verbose_name_plural = "Queues"

    barber = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='queue'
    )

    waiting_time = models.PositiveIntegerField(
        default=0
    )
        
class QueueEntry(models.Model):
    class Meta:
        verbose_name = "Queue Entry"
        verbose_name_plural = "Queue Entries"

    queue = models.ForeignKey(
        Queue,
        on_delete=models.CASCADE
    )

    uuid = models.CharField(
        max_length=36,
        default=uuid4()
    )

    timestamp = models.DateTimeField(
        auto_now_add=True
    )

    valid = models.BooleanField(
        default=True
    )
