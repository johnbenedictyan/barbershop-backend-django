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


def JoinQueue(request, queueId):
    barber_info = AccountDetails.objects.get(
        queue=queueId
    )
    if barber_info:
        queue_entry = QueueEntry.objects.get(
            queue=queueId
        )
        if not queue_entry:
            try:
                new_queue_entry = QueueEntry.objects.create(
                    queue=queueId,
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
                        queueId,
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
                    queueId
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

def LeaveQueue(request, queueId):
    barber_info = AccountDetails.objects.get(
        queue=queueId
    )
    if barber_info:
        uuid = request.session.get('uuid')
        if uuid:
            try:
                queue_entry = QueueEntry.objects.get(
                    queue=queueId,
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
                        queueId
                    )
                )
        else:
            return redirect(
                reverse(
                    'view_queue',
                    queueId
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

def ViewQueue(request, queueId):
    barber_info = AccountDetails.objects.get(
        queue=queueId
    )
    if barber_info:
        queue = QueueEntry.objects.filter(
            queue=queueId,
        ).order_by(
            'timestamp'
        )
        uuid = request.session.get('uuid')
        if uuid:
            try:
                queue_entry = QueueEntry.objects.get(
                    queue=queueId,
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
