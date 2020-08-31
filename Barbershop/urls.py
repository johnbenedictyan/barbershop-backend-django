"""Barbershop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Imports from django
from django.contrib import admin
from django.urls import include, path

# Imports from foreign installed apps
# from notifications.urls import urlpatterns as notifications_urls

# Imports from local apps
from barbers.urls import urlpatterns as barbers_urls
from website.urls import urlpatterns as website_urls
from queuer.urls import urlpatterns as queue_urls

# Start of Urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('barbers/', include(barbers_urls)),
    path('queue/', include(queue_urls)),
    path('', include(website_urls)),
]
