from rest_framework.serializers import ModelSerializer
from Tool.models import *
from Tool.serializers.user import UserSerializer

class StudentSerializer(ModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model = Student
        fields = '__all__'