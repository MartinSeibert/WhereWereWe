from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from main.models import Show, Episode
from main.forms import ShowForm, UserForm, UserProfileForm



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

def register(request):

	# A boolean value for telling the template whether the registration was successful.
	# Set to false initially. Code changes value to true when registration succeeds
	registered = False

	# If it's a HTTP POST, we're interested in processing form data.
	if request.method == 'POST':
		# Attempt to grab information from the raw form information.
		# Note that we make use of both UserFOrm and UserProfileForm
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		# If the two forms are valid...
		if user_form.is_valid() and profile_form.is_valid():
			# Save the user's form data to the database.
			user = user_form.save()

			# Now hash the password with the set_password method.
			# Once hashed, we can update the user object.
			user.set_password(user.password)
			user.save()

			# Now sort out the UserProfile instance.
			# Since we need to set the user attribute ourselves, we set commit=False.
			# This delays saving the model until we're ready to avoid integrity problems.
			profile = profile_form.save(commit=False)
			profile.user = user

			# Did the user provide a profile picture?
			# If so, we need to get it from the input form and put it in the UserProfile model

			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']

			# Now save the UserProfile model instance.
			profile.save()

			# Update our variable to tell the template registration was successful.
			registered = True

		# Invalid form or forms - mistakes or something else?
		# Print problems to the terminal.
		# They'll also be shown to the user.
		print user_form.errors, profile_form.errors

	# Not a HTTP POST, so we render our form using two ModelForm instances.
	# These forms will be blank, ready for user input.
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	# Render the template depending on the context.
	return render(request,
		'main/register.html',
		{'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

def user_login(request):

	# If the request is a HTTP POST, try to pull out the relevant information.
	if request.method == 'POST':
		# Gather the username and password provided by the user.
		# This information is obtained from the login form.
			# We use request.POST.get('<variable>') as opposed to request.POST['<variable>'], because the request.POST.get('<variable>') returns None if the value does not exist, while the request.POST['<variable>'] will raise key error exception
		username = request.POST.get('username')
		password = request.POST.get('password')

		# Use Django's machinery to attempt to see if the username/password combination is valid - a User object is returned if it is.
		user = authenticate(username=username, password=password)

		# If we have a User object, the details are correct.
		# If None (Python's way of representing the absence of a value), no user with matching credentials was found.
		if user:
			# Is the account active? It could have been disabled.
			if user.is_active:
				# If the account is valid and active, we can log the user in.
				# We'll send the user back to the homepage.
				login(request, user)
				return HttpResponseRedirect('/main/')
			else:
				# An inactive account was used, so they can't log in
				return HttpResponse("This account has been disabled or is no longer active")
		else:
			# Bad login details were provided
			# To display username and password, replace the print statement with print "Invalid login details: {0}, {1}".format(username, password)			
			print "Username or password is incorrect"
			return HttpResponse("Invalid login credentials provided.")

		# The request is not a HTTP POST, it's likely a GET so display the login form
	else:
		# No context variables to pass to the template system, hence the blank dictionary object
		return render(request, 'main/login.html', {})

# Use the login_required() decorator to ensure only those logged in can access the view.
# The @ denotes that this method is a PYTHON DECORATOR
@login_required
def user_logout(request):
	# Since we know the user is logged in, we can now just log them out.
	logout(request)

	# Take the user back to the homepage.
	return HttpResponseRedirect('/main/')