from django.shortcuts import render
from django.views import generic

from models import URL
from shortener import RedisServer, Shortener

class IndexView(generic.ListView):
	template_name = 'shortener/index.html'
	context_object_name = 'url_list'

	def get_queryset(self):
		"""Fetch the most recent ten URLs."""
		redis_server = RedisServer()
		return URL.objects.order_by('-craeted_at')[:10]


def shorten(request):
	if request.method == 'POST':
