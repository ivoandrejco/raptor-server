from datetime import date
from rest_framework import serializers
from .models import Diagnosis, Investigation


class DiagnosesSerializer(serializers.ModelSerializer):
    created_on = serializers.ReadOnlyField()

    def create(self, validated_data):
        validated_data['updated_on'] = date.today()
        validated_data['created_on'] = date.today()
        return super().create(validated_data)
        
    def update(self, instance, validated_data):
        validated_data['updated_on'] = date.today()
        return super().update(instance, validated_data)
        
    class Meta:
        model = Diagnosis
        fields = ['id', 'patient','kind','title', 'description','created_on']

 
class InvestigationsSerializer(serializers.ModelSerializer):
    created_on = serializers.ReadOnlyField()
    updated_on = serializers.ReadOnlyField()

    def create(self, validated_data):
        validated_data['updated_on'] = date.today()
        validated_data['created_on'] = date.today()
        return super().create(validated_data)
    
        
    def update(self, instance, validated_data):
        validated_data['updated_on'] = date.today()
        return super().update(instance,validated_data)
        
    def partial_update(self, instance, validated_data):
        validated_data['updated_on'] = date.today()
        return super().update(instance,validated_data)
    
    class Meta:
        model = Investigation
        fields = ['id', 'diagnosis','template','json','value','comment','updated_on','created_on']

