from rest_framework import serializers
from math import sqrt, pow
from datetime import date

from patients.models import Patient
from consultations.models import Consultation

from .models import Examination, BMI, IBW, ABW, BSA_D, BSA_M

class ExaminationSerializer(serializers.ModelSerializer):

    def create(self,validated_data):
        height          = validated_data['height']
        weight          = validated_data['weight']
        consultation    = validated_data['consultation']
        ibw     = 0

        if height == 0 or weight == 0:
            return super().create(validated_data)
        
        consult = Consultation.objects.get(pk=consultation)
        patient = Patient.objects.get(pk=consult.patient)
        gender  = patient.gender

        validated_data['BMI']   = BMI(height,weight)
        validated_data['IBW']   = IBW(gender,height,weight)
        validated_data['ABW']   = ABW(gender,height,weight)
        validated_data['BSA_D'] = BSA_D(height,weight)
        validated_data['BSA_M'] = BSA_M(height,weight)
        validated_data['collected_on'] = date.today()
        validated_data['created_on']   = date.today()

        return super().create(validated_data)

    class Meta:
        model = Examination
        fields = ['id','consultation','height','weight','pulse','pulse_desc','BP','temp','sats','findings','collected_on','updated_on']
