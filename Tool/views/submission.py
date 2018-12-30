from Tool.models import *
from Tool.serializers import *
from rest_framework.generics import *

class ListSubmissionsOfTask(ListCreateAPIView):
    serializer_class = SubmissionSerializer

    def get_queryset(self):
        return Submission.objects.filter(
            course__id=self.kwargs['c_id'],
            task__id=self.kwargs['t_id']
        )

class DetailSubmissionOfTask(RetrieveUpdateDestroyAPIView):
    queryset         = Submission.objects.all()
    serializer_class = SubmissionSerializer

    def get_object(self):
        queryset   = self.filter_queryset(self.get_queryset())
        conditions = {
            'course__id': self.kwargs['c_id'],
            'task__id': self.kwargs['t_id'],
            'id': self.kwargs['sub_id']
        }
        return get_object_or_404(queryset, **conditions)