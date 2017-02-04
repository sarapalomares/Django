from django.shortcuts import render
from . import models
# Create your views here.
def index(req):
    cities = models.Countries.objects.filter(languagetocountry__language='slovene')
    languages = models.Languages.objects.filter(language='slovene')

    # prints the queries
    print (50*"*")
    print cities.query
    print (50*"*")
    print languages.query
    print (50*"*")
    return render(req, 'worldApp/index.html', context={'cities':cities})
