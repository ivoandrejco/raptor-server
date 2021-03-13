from rest_framework import serializers
from rest_framework.response import Response
from .models import Consultation, Issue, Letter, Investigation
from patients.models import Patient
from doctors.serializers import ProviderNumberSerializer
from doctors.models import ProviderNumber
from datetime import date, datetime


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
        fields = ['id', 'iid','tid','title','json','value','comment','updated_on','created_on']


class IssuesSerializer(serializers.ModelSerializer):
    investigations  = InvestigationsSerializer(many=True,read_only=True)
    created_on      = serializers.ReadOnlyField()
    updated_on      = serializers.ReadOnlyField()

    def update(self, instance, validated_data):
        validated_data['updated_on'] = date.today()
        return super().update(instance,validated_data)
        
    def partial_update(self, instance, validated_data):
        validated_data['updated_on'] = date.today()
        return super().update(instance,validated_data)

    def create(self, validated_data):
        validated_data['updated_on'] = date.today()
        validated_data['created_on'] = date.today()
        return super().create(validated_data)
    
    class Meta:
        model   = Issue
        fields  = ['id', 'cid','tid','title','json','tags','presentation','conclusion','investigations','updated_on','created_on']

class LettersSerializer(serializers.ModelSerializer):
    created_on = serializers.ReadOnlyField()
    updated_on = serializers.ReadOnlyField()

    def create(self, validated_data):
        validated_data['created_on'] = date.today()
        validated_data['updated_on'] = date.today()
        return super().create(validated_data)
        
    
    def update(self, instance, validated_data):
        validated_data['updated_on'] = date.today()
        return super().update(instance,validated_data)
        
    def partial_update(self, instance, validated_data):
        validated_data['updated_on'] = date.today()
        return super().update(instance,validated_data)
        
    class Meta:
        model = Letter
        fields = ['id', 'cid','status','title', 'content','updated_on','created_on']

class PatientField(serializers.RelatedField):
    
    def get_queryset(self):
        return Patient.objects.all

    def to_representation(self,value):
        return {"name":value.__str__(),"id":value.id}
    
    def to_internal_value(self,data):
        return Patient.objects.get(pk=data)

class ProviderField(serializers.RelatedField):
    
    def get_queryset(self):
        return ProviderNumber.objects.all

    def to_representation(self,value):
        return {"doctor":f"{value.doctor.first_name} {value.doctor.last_name}","specialty":value.doctor.specialty,"number":value.number,"id":value.id}
    
    def to_internal_value(self,data):
        return ProviderNumber.objects.get(pk=data)

class ConsultationsSerializer(serializers.ModelSerializer):
    created_on  = serializers.ReadOnlyField()
    issues      = IssuesSerializer(many=True,read_only=True)
    letters     = LettersSerializer(many=True,read_only=True)
    #provider    = ProviderNumberSerializer(read_only=True)

    pid         = PatientField()
    provider    = ProviderField()

    def create(self, validated_data):
        validated_data['created_on'] = datetime.now()
        
        return super().create(validated_data)

    
    class Meta:
        model = Consultation
        fields = ['id', 'pid','code','provider','weight','height','BP','pulse','examination','presentation', 'plan','conclusion','issues','letters','created_on']
        
