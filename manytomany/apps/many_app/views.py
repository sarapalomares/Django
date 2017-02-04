from django.shortcuts import render, redirect
from .models import User
from .models import Interest

def index(request):
    return render(request, "many_app/index.html")

def create(request):
    f_name = request.POST['first_name']
    l_name = request.POST['last_name']
    interest = request.POST['interest']
    new_user = User.objects.create(first_name = f_name, last_name = l_name)
    new_interest = Interest.objects.create(name=interest)
    new_user.interests.add(new_interest)
    context = {
        "users" : User.objects.all()
    }
    return render(request, "many_app/result.html", context)
