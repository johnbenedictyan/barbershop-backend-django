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
    barber_info = AccountDetails.objects.get(
        barberId=barberId
    )
    if barber_info:
        queue_entry = QueueEntry.objects.get(
            barberId=barberId
        )
        if not queue_entry:
            try:
                new_queue_entry = QueueEntry.objects.create(
                    barberId=baberId,
                    uuid=uuid4()
                )
            except Exception as err:
                pass
            else:
                messages.success(
                    request,
                    f"You have successfully joined {barber_info.name}'s queue"
                )
                return redirect(
                    reverse(
                        'view_queue',
                        barberId,
                        new_queue_entry.id
                    )
                )
        else:
            messages.warning(
                request,
                f"You are already in {barber_info.name}'s queue"
            )
            return redirect(
                reverse(
                    'view_queue',
                    barberId
                )
            )
    else:
        messages.warning(
            request,
            f"This barber does not exist"
        )
        return redirect(
            reverse(
                'home'
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
                        request,
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
            request,
            f"This barber does not exist"
        )
        return redirect(
            reverse(
                'home'
            )
        )

def ViewQueue(request, barberId):
    barber_info = AccountDetails.objects.get(
        barberId=barberId
    )
    if barber_info:
        queue = QueueEntry.objects.filter(
            barberId=barberId,
        ).order_by(
            'timestamp'
        )
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
                    return render(
                        'view-queue.html',
                        {
                            queue,
                            uuid
                        }
                    )
        return render(
            'view-queue.html',
            {
                queue
            }
        )
    else:
        messages.warning(
            request,
            f"This barber does not exist"
        )
        return redirect(
            reverse(
                'home'
            )
        )
