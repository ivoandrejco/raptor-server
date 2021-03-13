from rest_framework import serializers
from .models import Medication, Allergy
from doctors.models import ProviderNumber
from datetime import date

class BilledBySerializer(serializers.RelatedField):
    def to_representation(self,obj):
        return obj.__str__()
    
    def to_internal_value(self,data):
        return ProviderNumber.objects.get(pk=data)

class MedicationsSerializer(serializers.ModelSerializer):
    created_on = serializers.ReadOnlyField()

    def create(self, validated_data):
        validated_data['created_on'] = date.today()
        validated_data['reviewed_on'] = date.today()
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if(validated_data.get('ceased')):
            validated_data['ceased_on'] = date.today()
        else:
            validated_data['ceased_on'] = None
                
        validated_data['reviewed_on'] = date.today()
        print(validated_data)
        return super().update(instance,validated_data)
        
    def partial_update(self, instance, validated_data):
        if(validated_data.get('ceased')):
            validated_data['ceased_on'] = date.today()
        else:
            validated_data['ceased_on'] = None

        validated_data['reviewed_on'] = date.today()
        print(validated_data)
        return super().update(instance,validated_data)

    class Meta:
        model = Medication
        fields = ['id', 'pid','name', 'dose', 'frequency','comment','ceased','ceased_on','created_on']

class AllergiesSerializer(serializers.ModelSerializer):
#    billed_by = BilledBySerializer(queryset=ProviderNumber.objects.all())

    class Meta:
        model = Allergy
        fields = ['id', 'pid', 'drug', 'reaction']

