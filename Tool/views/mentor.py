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
    queryset         = Mentor.objects.all()
    serializer_class = MentorSerializer

    def get_object(self):
        queryset   = self.filter_queryset(self.get_queryset())
        conditions = {
            'managedCourses__id': self.kwargs['c_id'],
            'id': self.kwargs['m_id']
        }
        return get_object_or_404(queryset, **conditions)

class ListSearchedMentors(ListCreateAPIView):
    def get_queryset(self):
        try:
            username = self.request.GET['username']
            if len(username) <= 0:
                raise Exception
            return Mentor.objects.filter(user__username__iregex=username)
        except:
            return Mentor.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MentorSerializer
        else:
            return MentorSignupSerializer

class DetailMentor(RetrieveUpdateDestroyAPIView):
    queryset         = Mentor.objects.all()
    lookup_field     = 'id'
    lookup_url_kwarg = 'm_id'

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MentorDetialSerializer
        else:
            return MentorSignupSerializer        