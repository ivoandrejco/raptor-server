from django.urls import path, include
from .models import Patient

#import rest_framework
from rest_framework import serializers

# Serializers define the API representation.
class PatientsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        fields = ['id', 'fname', 'lname', 'dob','gender']
        
