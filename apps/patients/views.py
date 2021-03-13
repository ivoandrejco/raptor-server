from django.shortcuts import render
from django.db.models import Q
from .models import Patient
from .serializers import PatientsSerializer
#import rest_framework
from rest_framework import viewsets

# ViewSets define the view behavior.
class PatientsViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientsSerializer

    def get_queryset(self):
        search = self.request.query_params.get('search')
        print(f"search item is : {search}")
        if search is not None:
            return Patient.objects.filter( Q(fname__icontains=search) | Q(lname__icontains=search) )
        else:
            return Patient.objects.all()

