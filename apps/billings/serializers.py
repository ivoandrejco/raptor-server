from rest_framework import serializers
from .models import Claim, ClaimPaid
from doctors.models import ProviderNumber

class BilledBySerializer(serializers.RelatedField):
    def to_representation(self,obj):
        return obj.__str__()
    
    def to_internal_value(self,data):
        return ProviderNumber.objects.get(pk=data)

class ClaimSerializer(serializers.ModelSerializer):
    billed_by = BilledBySerializer(queryset=ProviderNumber.objects.all())

    class Meta:
        model = Claim
        fields = ['id', 'fname', 'lname', 'code','amount','billed_on','billed_by','dob']

class ClaimPaidSerializer(serializers.ModelSerializer):
    billed_by = BilledBySerializer(queryset=ProviderNumber.objects.all())

    class Meta:
        model = ClaimPaid
        fields = ['id', 'fname', 'lname', 'code','amount','billed_on','billed_by','dob']

