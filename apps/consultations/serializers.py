from datetime import date, datetime
from rest_framework import serializers
from .models import Consultation, Letter, Examination
from .models import BMI, IBW, ABW, BSA_D, BSA_M, is_number
from patients.models import Patient
from doctors.serializers import ProviderNumberSerializer
from doctors.models import ProviderNumber


class ExaminationSerializer(serializers.ModelSerializer):
    collected_on    = serializers.ReadOnlyField()
    updated_on      = serializers.ReadOnlyField()

    
    def create(self,validated_data):
        height          = validated_data['height']
        weight          = validated_data['weight']
        gender          = validated_data['consultation'].patient.gender
        
        validated_data['BMI']   = BMI(height,weight)
        validated_data['IBW']   = IBW(height,gender)
        validated_data['ABW']   = ABW(height,weight,gender)
        validated_data['BSA_D'] = BSA_D(height,weight)
        validated_data['BSA_M'] = BSA_M(height,weight)
        validated_data['collected_on'] = date.today()
        validated_data['updated_on']   = date.today()
       
        return super().create(validated_data)

    class Meta:
        model = Examination
        fields = ['id','consultation','height','weight','pulse','pulse_desc','BP','temp','sats','sats_desc','findings','collected_on','updated_on']

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
    created_on      = serializers.ReadOnlyField()
    examinations    = ExaminationSerializer(many=True,read_only=True)
    letters         = LettersSerializer(many=True,read_only=True)
    #provider    = ProviderNumberSerializer(read_only=True)

    patient     = PatientField()
    provider    = ProviderField()

    def create(self, validated_data):
        validated_data['created_on'] = datetime.now()
        
        return super().create(validated_data)

    
    class Meta:
        model = Consultation
        fields = ['id', 'patient','code','provider','examinations','letters','history','impression', 'plan','created_on']
        
