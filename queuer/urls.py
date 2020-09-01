# Imports from django
from django.urls import path

# Imports from foreign installed apps

# Imports from local apps
from .views import (
    JoinQueue, LeaveQueue, ViewQueue, OpenQueue, CloseQueue, PauseQueue
)

# Start of Urls

urlpatterns = [
    path(
        'join/<int:queueId>',
        JoinQueue,
        name='join_queue'
    ),
    path(
        'leave/<int:queueId>',
        LeaveQueue,
        name='leave_queue'
    ),
    path(
        'view/<int:barberId>',
        ViewQueue,
        name='view_queue'
    ),
    path(
        'open/<int:queueId>',
        OpenQueue,
        name='open_queue'
    ),
    path(
        'close/<int:queueId>',
        CloseQueue,
        name='close_queue'
    ),
    path(
        'pause/<int:queueId>',
        PauseQueue,
        name='pause_queue'
    )
]
