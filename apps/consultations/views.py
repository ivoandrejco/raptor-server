from rest_framework import viewsets
from .models import Consultation, Issue, Letter, Investigation
from .serializers import ConsultationsSerializer, IssuesSerializer, InvestigationsSerializer, LettersSerializer
#from django_filters import rest_framework as filters

# ViewSets define the view behavior.
class ConsultationsViewSet(viewsets.ModelViewSet):
    queryset = Consultation.objects.all()
    serializer_class = ConsultationsSerializer
    filterset_fields = ("pid",)

class IssuesViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssuesSerializer
    filterset_fields = ("cid",)

class InvestigationsViewSet(viewsets.ModelViewSet):
    queryset = Investigation.objects.all()
    serializer_class = InvestigationsSerializer
    filterset_fields = ("iid",)

class LettersViewSet(viewsets.ModelViewSet):
    queryset = Letter.objects.all()
    serializer_class = LettersSerializer
    filterset_fields = ("cid",)
