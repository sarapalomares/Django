from django.shortcuts import render
from . import models

def index(request):
    context = {"no": True}
    return render(request, "disappearing_ninjas_app/index.html", context)

def ninjas(request):
    return render(request, "disappearing_ninjas_app/ninjas.html")

def color(request, color):
    turtle_options = {
        'red': 'images/raphael.png',
        'blue': 'images/leonardo.gif',
        'orange': 'images/michelangelo.png',
        'purple': 'images/donatello.gif',
    }
    if color in turtle_options:
        context = {
            'image':turtle_options[color]
        }
    else:
        context = {
            'image': 'images/rawr.jpg'
        }

    return render(request, "disappearing_ninjas_app/index.html", context)
