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

def ViewQueue(request, barberId):
    try:
        barber_info = AccountDetails.objects.get(
            user=barberId
        )
    except AccountDetails.DoesNotExist:
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
        queueId = Queue.objects.get(
            barber=barberId
        )
        queue_object = QueueEntry.objects.filter(
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
                if not queue_entry:
                    request.session.pop('uuid')
                    uuid = None
        return render(
            request,
            'queue.html',
            {
                'queue_object':queue_object,
                'barber_info':barber_info,
                'uuid':uuid
            }
        )

def OpenQueue(request, queueId):
    try:
        selected_queue = Queue.objects.get(
            barber=request.user
        )
    except Queue.DoesNotExist:
        messages.warning(
            request,
            f"This queue does not belong to you"
        )
        return redirect(
            reverse(
                'home'
            )
        )
    else:
        selected_queue.open = True
        selected_queue.save()
        messages.success(
            request,
            f"The queue is now open"
        )
        return redirect(
            reverse(
                'view_queue',
                queueId
            )
        )

def CloseQueue(request, queueId):
    try:
        selected_queue = Queue.objects.get(
            barber=request.user
        )
    except Queue.DoesNotExist:
        messages.warning(
            request,
            f"This queue does not belong to you"
        )
        return redirect(
            reverse(
                'home'
            )
        )
    else:
        selected_queue.open = False
        selected_queue.save()
        messages.success(
            request,
            f"The queue is now closed"
        )
        return redirect(
            reverse(
                'view_queue',
                queueId
            )
        )
