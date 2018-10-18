from rest_framework.serializers import ModelSerializer
from Tool.models import *

class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'