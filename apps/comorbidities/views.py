from rest_framework import viewsets
from .models import Comorbidity
from .serializers import ComorbiditiesSerializer

# ViewSets define the view behavior.
class ComorbiditiesViewSet(viewsets.ModelViewSet):
    queryset = Comorbidity.objects.all()
    serializer_class = ComorbiditiesSerializer
    filterset_fields = ("pid",)
