from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from registration.backends.simple.views import RegistrationView

# Create a new class that redirects the user to the index page when successfully registered
class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return '/main/'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'WhereWereWe_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^main/', include('main.urls')),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/', include('registration.backends.simple.urls')),		
)

# NOTE: this media declaration must be below the urlpatterns
# once deployed, this media serving will be handled by NGINX rather than django
if settings.DEBUG:
	urlpatterns += patterns(
		'django.views.static',
		(r'^media/(?P<path>.*)',
		'serve',
		{'document_root': settings.MEDIA_ROOT}), )