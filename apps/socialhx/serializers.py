from rest_framework import serializers
from .models import SocialHx
from datetime import date

class SocialHxSerializer(serializers.ModelSerializer):
    created_on = serializers.ReadOnlyField()

    class Meta:
        model = SocialHx
        fields = ['pid','living', 'working', 'smoking','drinking','children','family','template','template_value','created_on']

