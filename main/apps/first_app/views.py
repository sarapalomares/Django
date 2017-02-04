from django.shortcuts import render, HttpResponse

def index(request):
    print ("*"*10)
    return render(request, "first_app/index.html")
