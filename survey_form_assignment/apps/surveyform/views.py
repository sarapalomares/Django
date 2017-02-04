from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render(request, "surveyform/index.html")

def process(request):
    if 'counter' in request.session:
        request.session['counter'] +=1
    else:
        request.session['counter'] = 1

    request.session['name'] = request.POST['your_name'],
    request.session['dojo_location']= request.POST['location'],
    request.session['favorite_language']= request.POST['language'],
    request.session['comments']= request.POST['comment']
    print request.session['name']
    return redirect('/result')

def result(request):
    print "Go to show results!"
    print request.session
    return render(request, "surveyform/result.html")
