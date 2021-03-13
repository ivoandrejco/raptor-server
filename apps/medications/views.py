from rest_framework import viewsets
from .models import Medication, Allergy
from .serializers import MedicationsSerializer, AllergiesSerializer
#from django_filters import rest_framework as filters

# ViewSets define the view behavior.
class MedicationsViewSet(viewsets.ModelViewSet):
    queryset = Medication.objects.all()
    serializer_class = MedicationsSerializer
    filterset_fields = ("pid",)

# ViewSets define the view behavior.
class AllergiesViewSet(viewsets.ModelViewSet):
    queryset = Allergy.objects.all()
    serializer_class = AllergiesSerializer
    filterset_fields = ("pid",)
