from django.shortcuts import render
from . import models
# Create your views here.
def index(req):
    #practice chaining
    #1
    users = models.Users.objects.filter(last_name='rodriguez')
    #2
    users = models.Users.objects.exclude(last_name='rodriguez')
    #3
    users = models.Users.objects.filter(last_name='rodriguez') | models.Users.objects.filter(first_name='daniel')
    print users.query
    print users
    #end of add
    context = {
        'users':users
    }
    return render(req, "friendapp/index.html",context)
