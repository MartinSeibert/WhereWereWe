from django.conf.urls import patterns, url
from main import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^about/$', views.about, name='about'),
	url(r'^dagashiKashi/$', views.dagashiKashi, name='dagashiKashi'),
	url(r'^add_show/$', views.add_show, name='add_show'),
	url(r'^show/(?P<show_title_slug>[\w\-]+)/$', views.show, name='show'),


)