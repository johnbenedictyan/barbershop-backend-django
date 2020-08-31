# Imports from django
from django.urls import path

# Imports from foreign installed apps

# Imports from local apps
from .views import JoinQueue, LeaveQueue, ViewQueue

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
        'view/<int:queueId>',
        ViewQueue,
        name='view_queue'
    )
]
