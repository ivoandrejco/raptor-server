from rest_framework import serializers
from .models import Task
from datetime import datetime

from patients.models import Patient



class PatientField(serializers.RelatedField):
    
    def get_queryset(self):
        return Patient.objects.all

    def to_representation(self,value):
        return {"name":value.__str__(),"id":value.id}
    
    def to_internal_value(self,data):
        return Patient.objects.get(pk=data)

class TasksSerializer(serializers.ModelSerializer):
    pid         = PatientField()
    updated_on  = serializers.ReadOnlyField()
    created_on  = serializers.ReadOnlyField()

    def create(self, validated_data):
        validated_data['created_on'] = datetime.now()
        validated_data['updated_on'] = datetime.now()
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data['updated_on'] = datetime.now()
        return super().update(instance,validated_data)
        
    def partial_update(self, instance, validated_data):
        validated_data['updated_on'] = datetime.now()
        return super().update(instance,validated_data)
    
    class Meta:
        model = Task
        fields = ['id', 'pid','name', 'status','updated_on','created_on']
