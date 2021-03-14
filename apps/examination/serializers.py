from rest_framework import serializers
from math import sqrt, pow

from patients.models import Patient

from .models import Examination, BMI, IBW, ABW, BSA_D, BSA_M

class ExaminationSerializer(serializers.ModelSerializer):

    def create(self,validated_data):
        height  = validated_data['height']
        weight  = validated_data['weight']
        pid     = validated_data['pid']
        ibw     = 0

        if height == 0 or weight == 0:
            return super().create(validated_data)
        
        patient = Patient.objects.get(pk=pid)
        gender  = patient.gender

        validated_data['BMI']   = BMI(height,weight)
        validated_data['IBW']   = IBW(gender,height,weight)
        validated_data['ABW']   = ABW(gender,height,weight)
        validated_data['BSA_D'] = BSA_D(height,weight)
        validated_data['BSA_M'] = BSA_M(height,weight)

        return super().create(validated_data)

    class Meta:
        model = Examination
        fields = ['id','pid','height','weight','pulse','pulse_desc','BP','temp','sats','findings','collected_on','updated_on']
