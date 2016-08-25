from django.http import HttpResponse

def index(request):
	return HttpResponse('Hiya<br><a href="/main/about">About this site</a>')

def about(request):
	return HttpResponse('Developed by Martin Seibert.<a href="/main/">Return home</a>')