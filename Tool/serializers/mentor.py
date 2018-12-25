from rest_framework.serializers import ModelSerializer
from Tool.models import *
from Tool.serializers.user import UserSerializer, UserSignupSerializer

class MentorSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Mentor
        fields = '__all__'

class MentorSignupSerializer(ModelSerializer):
    user = UserSignupSerializer()

    class Meta:
        model = Mentor
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create(**validated_data.pop('user'), is_mentor=True)
        validated_data.pop('managedCourses')
        validated_data.pop('courseRequests')
        return Mentor.objects.create(user=user, **validated_data)
