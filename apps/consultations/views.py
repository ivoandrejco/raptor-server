from rest_framework import viewsets
from .models import Consultation, Letter, Examination 
from .serializers import ConsultationsSerializer, LettersSerializer, ExaminationSerializer

# ViewSets define the view behavior.
class ConsultationsViewSet(viewsets.ModelViewSet):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationsSerializer

class LettersViewSet(viewsets.ModelViewSet):
    queryset = Letter.objects.all()
    serializer_class = LettersSerializer

class ExaminationViewSet(viewsets.ModelViewSet):
    queryset = Examination.objects.all()
    serializer_class = ExaminationSerializer

