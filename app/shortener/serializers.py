from rest_framework import serializers

from .models import URL

class URLSerializer(serializers.ModelSerializer):
	class Meta:
		model = URL
		fields = ('id', 'long_url', 'short_url', 'created_at',)
