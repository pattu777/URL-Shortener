from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible
from django.db import models

@python_2_unicode_compatible
class URL(models.Model):
	original_url = models.URLField()
	short_url = models.URLField()
	created_at = models.DateTimeField()

	def __str__(self):
		return self.original_url