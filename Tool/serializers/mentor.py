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

    def update(self, instance, validated_data):
        user                   = validated_data.pop('user')
        instance.user.username = user.get('username', instance.user.username)
        instance.user.email    = user.get('email', instance.user.email)
        instance.user.password = user.get('password', instance.user.password)
        instance.managedCourses.set(validated_data.pop('managedCourses'))
        instance.courseRequests.set(validated_data.pop('courseRequests'))
        instance.save()
        return instance