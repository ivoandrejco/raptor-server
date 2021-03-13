from rest_framework import serializers
from .models import Comorbidity

class ComorbiditiesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comorbidity
        fields = ['id', 'pid', 'name', 'comment']

