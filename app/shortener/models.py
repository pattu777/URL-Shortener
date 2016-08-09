from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.utils import timezone


@python_2_unicode_compatible
class URL(models.Model):
	long_url = models.URLField()
	short_url = models.URLField()
	created_at = models.DateTimeField(default=timezone.now())

	def __str__(self):
		return self.long_url