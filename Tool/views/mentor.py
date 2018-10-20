from Tool.models import *
from Tool.serializers import *
from rest_framework.generics import *

class ListMentorsOfCourse(ListCreateAPIView):
    serializer_class = MentorSerializer

    def get_queryset(self):
        return Mentor.objects.filter(
            managedCourses__id=self.kwargs['c_id']
        )

class DetailMentorOfCourse(RetrieveUpdateDestroyAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        conditions = {
            'managedCourses__id': self.kwargs['c_id'],
            'id': self.kwargs['m_id']
        }
        return get_object_or_404(queryset, **conditions)

class ListMentors(ListCreateAPIView):
    serializer_class = MentorSerializer
    queryset = Mentor.objects.all()

class DetailMentor(RetrieveUpdateDestroyAPIView):
    serializer_class = MentorSerializer
    queryset = Mentor.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'm_id'