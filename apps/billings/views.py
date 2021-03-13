from rest_framework import viewsets
from .models import Claim, ClaimPaid
from .serializers import ClaimSerializer, ClaimPaidSerializer

# ViewSets define the view behavior.
class ClaimViewSet(viewsets.ModelViewSet):
    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer

class ClaimPaidViewSet(viewsets.ModelViewSet):
    queryset = ClaimPaid.objects.all()
    serializer_class = ClaimPaidSerializer

