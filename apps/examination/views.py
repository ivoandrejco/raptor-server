from rest_framework import viewsets

from .models import Examination
from .serializers import ExaminationSerializer

# Create your views here.
class ExaminationViewSet(viewsets.ModelViewSet):
    queryset = Examination.objects.all()
    serializer_class = ExaminationSerializer

