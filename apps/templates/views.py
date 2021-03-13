from rest_framework import viewsets
from .models import Investigation, Issue
from .serializers import InvestigationsSerializer, IssuesSerializer

# ViewSets define the view behavior.
class InvestigationsViewSet(viewsets.ModelViewSet):
    queryset = Investigation.objects.all()
    serializer_class = InvestigationsSerializer

    def get_queryset(self):
        title = self.request.query_params.get("title")
        
        if title:
            return Investigation.objects.filter(slug__icontains=title)
        else:
            return Investigation.objects.all()


class IssuesViewSet(viewsets.ModelViewSet):
    queryset            = Issue.objects.all()
    serializer_class    = IssuesSerializer

    def get_queryset(self):
        title = self.request.query_params.get("title")
        
        if title:
            return Issue.objects.filter(slug__icontains=title)
        else:
            return Issue.objects.all()