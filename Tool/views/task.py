from Tool.models import *
from Tool.serializers import *
from rest_framework.generics import *

class ListTasksOfCourse(ListCreateAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(course__id=self.kwargs['c_id'])

class DetailTaskOfCourse(RetrieveDestroyAPIView):
    queryset         = Task.objects.all()
    serializer_class = TaskSerializer

    def get_object(self):
        queryset   = self.filter_queryset(self.get_queryset())
        conditions = {
            'course__id': self.kwargs['c_id'],
            'id': self.kwargs['t_id']
        }
        return get_object_or_404(queryset, **conditions)