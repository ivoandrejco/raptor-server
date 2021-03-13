from rest_framework import viewsets
from .models import SocialHx
from .serializers import SocialHxSerializer

# ViewSets define the view behavior.
class SocialHxViewSet(viewsets.ModelViewSet):
    queryset = SocialHx.objects.all()
    serializer_class = SocialHxSerializer
    filterset_fields = ("pid",)
