from rest_framework import viewsets
from .models import Diagnosis, Investigation
from .serializers import DiagnosesSerializer, InvestigationsSerializer

# ViewSets define the view behavior.
class DiagnosesViewSet(viewsets.ModelViewSet):
    queryset = Diagnosis.objects.all()
    serializer_class = DiagnosesSerializer

class InvestigationsViewSet(viewsets.ModelViewSet):
    queryset = Investigation.objects.all()
    serializer_class = InvestigationsSerializer

