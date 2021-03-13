
from django.urls import path, include
from .serializers import ProviderNumberSerializer
from .models import ProviderNumber

#import rest_framework
from rest_framework import viewsets

# ViewSets define the view behavior.
class ProviderNumberViewSet(viewsets.ModelViewSet):
    queryset = ProviderNumber.objects.all()
    serializer_class = ProviderNumberSerializer

# Routers provide an easy way of automatically determining the URL conf.
#router = routers.DefaultRouter()
#router.register(r'', BillingsActualViewSet)


#urlpatterns = [
    # Wire up our API using automatic URL routing.
    # Additionally, we include login URLs for the browsable API.
#    path('', include(router.urls)),
#]
