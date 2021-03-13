from rest_framework import viewsets
from .models import Diagnosis
from .serializers import DiagnosesSerializer

# ViewSets define the view behavior.
class DiagnosesViewSet(viewsets.ModelViewSet):
    queryset = Diagnosis.objects.all()
    serializer_class = DiagnosesSerializer
    filterset_fields = ("pid",)
