from rest_framework import serializers
from .models import ProviderNumber

class ProviderNumberSerializer(serializers.ModelSerializer):
    doctor      = serializers.StringRelatedField()
    practice    = serializers.StringRelatedField()
    class Meta:
        model = ProviderNumber
        fields = ['id','number','doctor','practice']
