from django.conf.urls import url
from main import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^about/$', views.about, name='about'),
	url(r'^add_show/$', views.add_show, name='add_show'),
	url(r'^show/(?P<series_id>[\w\-]+)/$', views.show, name='show'),
	url(r'^register/$', views.register, name='register'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^search/(?P<search_text>[\w\-]+)/$', views.search, name='search'),
	url(r'^search/$', views.search, name='search'),
]