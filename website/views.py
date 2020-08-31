# Imports from python

# Imports from django
from django.contrib import messages
from django.shortcuts import render, redirect

# Imports from foreign installed apps

# Imports from local apps

# Start of Views


def home(request):
    return render(
        request,
        'home.html'
    )