from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from registration.backends.simple.views import RegistrationView


urlpatterns = [
 	url(r'^admin/', admin.site.urls),
  url(r'^', include('main.urls')),   
]
               


