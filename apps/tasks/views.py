from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Task
from .serializers import TasksSerializer
#from django_filters import rest_framework as filters

# ViewSets define the view behavior.
class TasksViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TasksSerializer
    filterset_fields = ("pid",)

    def create(self,request,pk=None):
        print(TasksSerializer(data=request.data))
        return super().create(request)
