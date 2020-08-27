from django.shortcuts import render, redirect

# Create your views here.


def JoinQueue(request, barberId):
    return redirect(reverse('view_queue', barberId))


def LeaveQueue(request, barberId):
    return redirect(reverse('view_queue', barberId))


def ViewQueue(request, barberId):
    return render(request, 'queue.html', {
        'queue':queue
    })
