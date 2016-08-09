from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import URL
from .forms import URLForm
from .serializers import URLSerializer
from .shortener import RedisServer, Shortener


@api_view(['GET'])
def url_list(request):
	"""
	API endpoint to get a list of urls.
	"""
	if request.method == 'GET':
		urls = URL.objects.all().order_by('-created_at')
		serializer = URLSerializer(urls, many=True)
		return Response(serializer.data)


@api_view(['GET'])
def get_url(request, pk):
	"""
	API endpoint to fetch a single URL.
	"""
	url = get_object_or_404(URL, pk=pk)
	
	if request.method == 'GET':
		serializer = URLSerializer(url)
		return Response(serializer.data)


@api_view(['POST'])
def url_shorten(request):
	"""
	API endpoint to shorten a URL.
	"""
	if request.method == 'POST':
		serializer = URLSerializer(data=request.POST)
		if serializer.is_valid():
			serializer.save()

			print "Original URL %s" % (serializer.long_url)
			print "Current URL id %s" % (serializer.id)
			serializer.short_url = Shortener(url=serializer.long_url).shorten(current_id=serializer.id)
			print "Short URL is %s" % (serializer.short_url)

			# Save the values in DB.
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




def shorten(request):
	"""
	API endpoint to shorten a url or present a shortener form.
	"""
	if request.method == 'POST':
		form = URLForm(request.POST)
		if form.is_valid():
			url = form.save()

			# Fetch the original long URL from form.
			#url.created_at = timezone.now()
			
			# Shorten the long URL.
			print "Original URL %s" % (url.long_url)
			print "Current URL id %s" % (url.id)
			url.short_url = Shortener(url=url.long_url).shorten(current_id=url.id)
			print "Short URL is %s" % (url.short_url)

			# Save the values in DB.
			url.save()
			return HttpResponseRedirect(reverse("shortener:new"))
	else:
		form = URLForm()

	return render(request, 'shortener/new.html', {'form' : form})

