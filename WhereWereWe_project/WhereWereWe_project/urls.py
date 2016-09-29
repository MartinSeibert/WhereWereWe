from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from registration.backends.simple.views import RegistrationView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'WhereWereWe_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^main/', include('main.urls')),               
)

# NOTE: this media declaration must be below the urlpatterns
# once deployed, this media serving will be handled by NGINX rather than django
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
{'document_root': settings.MEDIA_ROOT}), )