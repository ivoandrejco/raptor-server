from rest_framework import viewsets
from .models import Schema
from .serializers import SchemasSerializer

# ViewSets define the view behavior.
class SchemasViewSet(viewsets.ModelViewSet):
    queryset = Schema.objects.all()
    serializer_class = SchemasSerializer

    def get_queryset(self):
        kind = self.request.query_params.get("kind")

        if kind:
            return Schema.objects.filter(kind__icontains=kind)
        else:
            return Schema.objects.all()


