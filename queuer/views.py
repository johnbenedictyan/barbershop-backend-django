# Imports from python
from uuid import uuid4

# Imports from django
from django.contrib import messages
from django.shortcuts import render, redirect

# Imports from foreign installed apps

# Imports from local apps
from .models import QueueEntry

# Start of Views


def JoinQueue(request, barberId):
    try:
        QueueEntry.objects.get(
            barberId=barberId
        )
    except Exception as err:
        pass
    else:
        try:
            new_queue_entry = QueueEntry.objects.create(
                barberId=baberId,
                uuid=uuid4()
            )
        except Exception as err:
            pass
        else:
            return redirect(
                reverse(
                    'view_queue',
                    barberId,
                    new_queue_entry.id
                )
            )
        return redirect(
            reverse(
                'view_queue',
                barberId
            )
        )

def LeaveQueue(request, barberId):
    return redirect(reverse('view_queue', barberId))


def ViewQueue(request, barberId):
    return render(request, 'queue.html', {
        'queue':queue
    })
