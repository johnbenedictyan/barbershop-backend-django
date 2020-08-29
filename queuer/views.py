# Imports from python
from uuid import uuid4

# Imports from django
from django.contrib import messages
from django.shortcuts import render, redirect

# Imports from foreign installed apps

# Imports from local apps
from barbers.models import AccountDetails
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
    barber_info = AccountDetails.objects.get(
        barberId=barberId
    )
    if barber_info:
        uuid = request.session.get('uuid')
        if uuid:
            try:
                queue_entry = QueueEntry.objects.get(
                    barberId=barberId,
                    uuid=uuid
                )
            except Exception as err:
                pass
            else:
                if queue_entry:
                    queue_entry.delete()
                    messages.success(
                        self.request,
                        f"You have successfully left {barber_info.name}'s queue"
                    )
                else:
                    pass
                return redirect(
                    reverse(
                        'view_queue',
                        barberId
                    )
                )
        else:
            return redirect(
                reverse(
                    'view_queue',
                    barberId
                )
            )
    else:
        messages.warning(
            self.request,
            f"This barber does not exist"
        )
        return redirect(
            reverse(
                'home'
            )
        )

def ViewQueue(request, barberId):
    return render(request, 'queue.html', {
        'queue':queue
    })
