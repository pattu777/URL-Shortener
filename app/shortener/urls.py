from django.conf.urls import url

import views

app_name = 'shortener'

urlpatterns = [
	url(r'$', views.IndexView.as_view(), namespace='index'),
	#url(r'new/', views.shorten, namespace='shorten')
]
