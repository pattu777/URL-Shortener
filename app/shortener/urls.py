from django.conf.urls import url
from rest_framework import routers

import views

app_name = 'shortener'

urlpatterns = [
	#url(r'$', views.IndexView.as_view(), name='index'),
	url(r'^$', views.shorten, name='new')
]
