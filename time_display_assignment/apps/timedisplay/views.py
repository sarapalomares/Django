from django.shortcuts import render, HttpResponse
from django.utils.timezone import utc
import datetime

def index(request):
	time = datetime.datetime.utcnow().replace(tzinfo=utc).strftime('%b %d, %Y, %I:%M:%S ' ' %p')
	context = {
		'currentTime' : time,
	}
	return render(request, 'timedisplay/index.html', context)
