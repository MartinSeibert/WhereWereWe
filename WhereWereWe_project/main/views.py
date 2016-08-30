from django.http import HttpResponse
from django.shortcuts import render
from main.models import Show

def index(request):

	# construct a dictionary to pass to the template engine as its context.
	
	# query the database for a list of all shows currently stored.
	# order the categories alphabetically by title
	# retrieve only the top 5
	show_list = Show.objects.order_by('title')[:5]
	context_dict = {'shows': show_list}

	# return a rendered response to send to the client
	# second parameter is the template, third is the context dictionary

	return render(request, 'main/index.html', context_dict)
	

def shows(request):

	context_dict = {'title': "DAGASHI KASHI"}

	return render(request, 'main/shows.html', context_dict)

def about(request):
	return HttpResponse('Developed by Martin Seibert.<a href="/main/">Return home</a>')