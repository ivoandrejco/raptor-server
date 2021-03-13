from rest_framework import serializers
from .models import Diagnosis
from datetime import date


class DiagnosesSerializer(serializers.ModelSerializer):
    created_on = serializers.ReadOnlyField()

    def create(self, validated_data):
        validated_data['created_on'] = date.today()
        return super().create(validated_data)
        
    class Meta:
        model = Diagnosis
        fields = ['id', 'pid','kind','title', 'description','created_on']
