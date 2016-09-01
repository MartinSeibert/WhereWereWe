from django.http import HttpResponse
from django.shortcuts import render
from main.models import Show, Episode
from main.forms import ShowForm


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
	

def dagashiKashi(request):

	context_dict = {'title': "DAGASHI KASHI"}

	return render(request, 'main/dagashiKashi.html', context_dict)

def about(request):
	return HttpResponse('Developed by Martin Seibert.<a href="/main/">Return home</a>')

def show(request, show_title_slug):

	# create a context dictionary which we can pass to the template rendering engine
	context_dict = {}

	try: 
		# Can we find a show title slug with the given title?
		# If we can't, the .get() method raises a DoesNotExist exception.
		show = Show.objects.get(slug=show_title_slug)
		context_dict['show_title'] = show.title

		# Retrieve all of the associated episodes.
		# Note that the filter returns >= 1 model instance.
		episodes = Episode.objects.filter(show = show)
		context_dict['episodes'] = episodes
		context_dict['show'] = show
	except Show.DoesNotExist:
		# we get here if we didn't find the specified show.
		# don't do anything - the template displays the "no show" message for us.
		pass

	# Go render the response and return it to the client.
	return render(request, 'main/show.html', context_dict)

def add_show(request):

	if request.method == 'POST':
		form = ShowForm(request.POST)

		# Have we been provided with a valid form?
		if form.is_valid():
			# save the new category to the database
			form.save(commit=True)

			# Now call the index() view.
			# The user will be shown the homepage
			return index(request)
		else:
			# The supplied form contained errors - just print them to the terminal.
			print form.errors
	else:
		# If the request was not a POST, display the form to enter details.
		form = ShowForm()

	return render(request, 'main/add_show.html', {'form': form})