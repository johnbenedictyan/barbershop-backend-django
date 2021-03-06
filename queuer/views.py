# Imports from python
from uuid import uuid4

# Imports from django
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

# Imports from foreign installed apps

# Imports from local apps
from users.models import AccountDetails
from .models import Queue, QueueEntry

# Start of Views


def JoinQueue(request, queueId):
    try:
        selected_queue = Queue.objects.get(pk=queueId)
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
        if selected_queue.opened == False or selected_queue.paused == True:
            messages.warning(
                request,
                f"""
                {selected_queue.barber.details.name}'s queue is closed
                """
            )
        else:
            uuid = request.session.get('uuid')
            if uuid:
                try:
                    queue_entry = QueueEntry.objects.get(
                        queue=selected_queue,
                        uuid=uuid
                    )
                except QueueEntry.DoesNotExist:
                    request.session.pop('uuid')
                    messages.warning(
                        request,
                        f"""
                        An error has occured when trying to join
                        {selected_queue.barber.details.name}'s queue
                        """
                    )
                else:
                    messages.warning(
                        request,
                        f"""
                        You are already in 
                        {selected_queue.barber.details.name}'s queue
                        """
                    )
            else:
                try:
                    new_queue_entry = QueueEntry.objects.create(
                        queue=selected_queue
                    )
                except Exception as err:
                    pass
                else:
                    request.session['uuid'] = str(new_queue_entry.uuid)
                    messages.success(
                        request,
                        f"""
                        You have successfully joined 
                        {selected_queue.barber.details.name}'s queue
                        """
                    )
        return redirect(
            reverse(
                'view_queue',
                kwargs={
                    'barberId': selected_queue.barber.id
                }
            )
        )


def LeaveQueue(request, queueId):
    try:
        selected_queue = Queue.objects.get(pk=queueId)
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
                    queue=selected_queue,
                    uuid=uuid
                )
            except QueueEntry.DoesNotExist:
                messages.warning(
                    request,
                    f"""
                    You have already left {selected_queue.barber.details.name}'s
                    queue
                    """
                )
            else:
                if queue_entry:
                    queue_entry.delete()
                    request.session.pop('uuid')
                    messages.success(
                        request,
                        f"""
                        You have successfully left 
                        {selected_queue.barber.details.name}'s queue
                        """
                    )
                else:
                    request.session.pop('uuid')
        return redirect(
            reverse(
                'view_queue',
                kwargs={
                    'barberId': selected_queue.barber.id
                }
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
        try:
            selected_queue = Queue.objects.get(
                barber=barberId
            )
        except Queue.DoesNotExist:
            messages.warning(
                request,
                f"This barber has not created a queue"
            )
            return redirect(
                reverse(
                    'home'
                )
            )
        else:
            queue_object = QueueEntry.objects.filter(
                queue=selected_queue,
            ).order_by(
                'timestamp'
            )
            if barberId == request.user.id:
                return render(
                    request,
                    'queue-admin.html',
                    {
                        'queue_object': queue_object,
                        'barber_info': barber_info,
                        'queue': selected_queue
                    }
                )
            uuid = request.session.get('uuid')
            wait_time = None
            if uuid:
                try:
                    queue_entry = QueueEntry.objects.get(
                        queue=selected_queue,
                        uuid=uuid
                    )
                except QueueEntry.DoesNotExist:
                    request.session.pop('uuid')
                    uuid = None
                else:
                    wait_time = queue_entry.wait_time
            return render(
                request,
                'queue.html',
                {
                    'queue_object': queue_object,
                    'barber_info': barber_info,
                    'uuid': uuid,
                    'queue': selected_queue,
                    'wait_time': wait_time
                }
            )


def SearchQueue(request):
    if request.method == 'POST':
        uuid = request.POST.get('uuid')
        if uuid:
            try:
                barber_info = AccountDetails.objects.get(
                    uuid=uuid
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
                barber_id = barber_info.user.id
                return redirect(
                    reverse(
                        'view_queue',
                        args=(barber_id,)
                    )
                )
    return redirect(
        reverse(
            'home'
        )
    )

@login_required
def OpenQueue(request, queueId):
    try:
        selected_queue = Queue.objects.get(pk=queueId)
    except Queue.DoesNotExist:
        messages.warning(
            request,
            f"This queue does not exist"
        )
        return redirect(
            reverse(
                'home'
            )
        )
    else:
        if selected_queue.barber == request.user:
            selected_queue.opened = True
            selected_queue.save()
            messages.success(
                request,
                f"The queue is now open"
            )
        else:
            messages.warning(
                request,
                f"This queue does not belong to you"
            )
        return redirect(
            reverse(
                'view_queue',
                kwargs={
                    'barberId': selected_queue.barber.id
                }
            )
        )


@login_required
def CloseQueue(request, queueId):
    try:
        selected_queue = Queue.objects.get(pk=queueId)
    except Queue.DoesNotExist:
        messages.warning(
            request,
            f"This queue does not exist"
        )
        return redirect(
            reverse(
                'home'
            )
        )
    else:
        if selected_queue.barber == request.user:
            selected_queue.max_queue_number = 0
            selected_queue.opened = selected_queue.paused = False
            selected_queue.save()
            QueueEntry.objects.filter(queue=selected_queue).delete()
            messages.success(
                request,
                f"The queue is now closed"
            )
        else:
            messages.warning(
                request,
                f"This queue does not belong to you"
            )
        return redirect(
            reverse(
                'view_queue',
                kwargs={
                    'barberId': selected_queue.barber.id
                }
            )
        )


@login_required
def PauseQueue(request, queueId):
    try:
        selected_queue = Queue.objects.get(pk=queueId)
    except Queue.DoesNotExist:
        messages.warning(
            request,
            f"This queue does not exist"
        )
        return redirect(
            reverse(
                'home'
            )
        )
    else:
        if selected_queue.barber == request.user:
            selected_queue.paused = True
            selected_queue.save()
            messages.success(
                request,
                f"The queue is now closed"
            )
        else:
            messages.warning(
                request,
                f"This queue does not belong to you"
            )
        return redirect(
            reverse(
                'view_queue',
                kwargs={
                    'barberId': selected_queue.barber.id
                }
            )
        )


@login_required
def KickFromQueue(request, queueId, queueEntryId):
    try:
        selected_queue = Queue.objects.get(pk=queueId)
    except Queue.DoesNotExist:
        messages.warning(
            request,
            f"This queue does not exist"
        )
        return redirect(
            reverse(
                'home'
            )
        )
    else:
        if selected_queue.barber == request.user:
            try:
                queue_entry = QueueEntry.objects.get(
                    pk=queueEntryId
                )
            except QueueEntry.DoesNotExist:
                pass
            else:
                queue_entry.delete()
                messages.success(
                    request,
                    f"""
                    You have successfully kicked this customer from the queue
                    """
                )
        else:
            messages.warning(
                request,
                f"This queue does not belong to you"
            )
        return redirect(
            reverse(
                'view_queue',
                kwargs={
                    'barberId': selected_queue.barber.id
                }
            )
        )


@login_required
def CreateQueue(request):
    try:
        selected_queue = Queue.objects.get(barber=request.user)
    except Queue.DoesNotExist:
        try:
            selected_account_details = AccountDetails.objects.get(
                user=request.user
            )
        except AccountDetails.DoesNotExist:
            messages.warning(
                request,
                f"Please update your account details before creating a queue"
            )
            return redirect(
                reverse(
                    'account_details'
                )
            )
        else:
            try:
                new_queue = Queue.objects.create(
                    barber=request.user
                )
            except Exception as err:
                messages.warning(
                    request,
                    f"An error has occurred when trying to create this queue"
                )
                return redirect(
                    reverse(
                        'home'
                    )
                )
            else:
                messages.success(
                    request,
                    f"Your queue has been successfully created"
                )
    else:
        messages.warning(
            request,
            f"A queue in your account already exist"
        )
    return redirect(
        reverse(
            'view_queue',
            kwargs={
                'barberId': request.user.id
            }
        )
    )
