# Imports from python
from uuid import uuid4

# Imports from django
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
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

    open = models.BooleanField(
        default=False
    )

    max_position = models.PositiveIntegerField(
        default=1
    )

    def __str__(self):
        return f"{self.barber.details.name}'s queue'"

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
        default=uuid4
    )

    timestamp = models.DateTimeField(
        auto_now_add=True
    )

    valid = models.BooleanField(
        default=True
    )

    position = models.PositiveIntegerField(
        default=0
    )

    def __str__(self):
        return f"Queue #{self.queue.id} Position #{self.position}"

    def save(self, *args, **kwargs):
        self.position = self.queue.max_position + 1
        super().save(*args, **kwargs)

@receiver(post_save, sender=QueueEntry)
def move_max_position(sender, instance, **kwargs):
    queue = instance.queue
    queue.max_position += 1
    queue.save()
    