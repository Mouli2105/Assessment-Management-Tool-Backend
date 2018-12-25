from rest_framework.serializers import ModelSerializer
from Tool.models import *
from Tool.serializers.user import UserSerializer, UserSignupSerializer

class StudentSerializer(ModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model = Student
        fields = '__all__'

class StudentSignupSerializer(ModelSerializer):
    user = UserSignupSerializer()
    
    class Meta:
        model = Student
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create(**validated_data.pop('user'), is_student=True)
        validated_data.pop('optedCourses')
        validated_data.pop('registrations')
        return Student.objects.create(user=user, **validated_data)