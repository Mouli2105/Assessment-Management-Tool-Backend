from Tool.models import *
from Tool.serializers import *
from rest_framework.generics import *

class ListCourses(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
