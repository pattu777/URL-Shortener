import string
import timezone

import redis

DOMAIN_NAME = 'localhost'


class RedisServer(object):
	def __init__(self, host='localhost', port=6739):
		self.host = host
		self.port = port
		self.server = redis.StrictRedis(host='localhost', port=6379, db=0)
		
		# Set the global counter of urls to 0.
		self.server.set('current.url.id', 0)

		# Create a redis list to contain ten most recent URLs.
		self.server.set('recent_urls', [None]*10)

	def get_current_id(self):
		return self.server.get('current.url.id')

	def insert_url(self, long_url, short_url):
		self.server.set(short_url, {'long_url': long_url, 'created_at': timezone.now()})
		url_list = self.server.get('recent_urls')
		url_list.pop()
		url_list.insert(0, short_url)
		self.server.set('recent_urls', url_list)

	def latest(self):
		"""Fetches a list of ten most recent URLs."""
		return self.recent_urls


class Shortener(object):
	def __init__(self, url=None):
		self.url = url
		self.base32 = {i: x for i, x in enumerate(string.ascii_lowercase)}
		self.base32.update({x+26:x for x in xrange(10)})

	def shorten(self):
		"""Return a shortened URL."""
		r_key = self.r.get_current_id()
		short_url = ""
		digits = []
		while r_key > 0:
			remainder = r_key % 62
			digits.append(remainder)
			r_key = r_key / 62

		for x in reversed(digits):
			short_url += self.base32[x]

		return short_url
