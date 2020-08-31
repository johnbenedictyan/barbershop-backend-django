# Imports from python
from uuid import uuid4

# Imports from django
from django.contrib import messages
from django.shortcuts import render, redirect

# Imports from foreign installed apps

# Imports from local apps
from barbers.models import AccountDetails
from .models import Queue, QueueEntry

# Start of Views


def JoinQueue(request, queueId):
    try:
        Queue.objects.get(pk=queueId)
    except Queue.DoesNotExist:
        messages.warning(
            request,
            f"This barber does not exist"
        )
        return redirect(
            reverse(
                'home'
            )
        )
    else:
        try:
            queue_entry = QueueEntry.objects.get(
                queue=queueId
            )
        except QueueEntry.DoesNotExist:
            try:
                new_queue_entry = QueueEntry.objects.create(
                    queue=queueId,
                    uuid=uuid4()
                )
            except Exception as err:
                pass
            else:
                request.session['uuid'] = new_queue_entry.uuid
                messages.success(
                    request,
                    f"You have successfully joined {barber_info.name}'s queue"
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
                f"You are already in {barber_info.name}'s queue"
            )
            return redirect(
                reverse(
                    'view_queue',
                    queueId
                )
            )

def LeaveQueue(request, queueId):
    try:
        Queue.objects.get(pk=queueId)
    except Queue.DoesNotExist:
        messages.warning(
            request,
            f"This barber does not exist"
        )
        return redirect(
            reverse(
                'home'
            )
        )
    else:
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
                    request.session.pop('uuid')
                    messages.success(
                        request,
                        f"You have successfully left {barber_info.name}'s queue"
                    )
                else:
                    request.session.pop('uuid')
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

def ViewQueue(request, queueId):
    barber = Queue.objects.get(pk=queueId).barber

    barber_info = AccountDetails.objects.get(
        barber=barber
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
