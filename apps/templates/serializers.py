from rest_framework import serializers
from .models import Issue, Investigation


class InvestigationsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Investigation
        fields = ['id','title','json','tags','comment']


class IssuesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Issue
        fields = ['id','title','slug','json','tags','presentation','conclusion','differential']
