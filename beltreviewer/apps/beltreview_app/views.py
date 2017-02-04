from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, "beltreview_app/index.html")

def registration(request):
    pass

def login(request):
    pass
