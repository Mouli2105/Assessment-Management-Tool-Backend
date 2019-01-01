from Tool.models import *
from Tool.serializers import *
from rest_framework.generics import *

class ListSearchedCourses(ListCreateAPIView):
    def get_queryset(self):
        try:
            name = self.request.GET['name']
            if len(name) <= 0:
                raise Exception
            return Course.objects.filter(name__iregex=name)
        except:
            return Course.objects.all()

    serializer_class = CourseSerializer

class DetailCourse(RetrieveUpdateDestroyAPIView):
    queryset         = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field     = 'id'
    lookup_url_kwarg = 'c_id'

# class ListOptedCourses(ListAPIView):
#     serializer_class = CourseSerializer

#     def get_queryset(self):
#         return Course.objects.filter(students__id=self.kwargs['s_id'])

# class ListManagedCourses(ListAPIView):
#     serializer_class = CourseSerializer

#     def get_queryset(self):
#         return Course.objects.filter(mentors__id=self.kwargs['m_id'])

class ListCourseRegistrations(ListAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        return Course.objects.get(id=self.kwargs['c_id']).studentRequests.all()