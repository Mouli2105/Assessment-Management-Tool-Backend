from rest_framework.serializers import ModelSerializer
from Tool.models import *
from Tool.serializers.user import UserSerializer, UserSignupSerializer

class MentorSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model  = Mentor
        fields = ('id', 'user')
        depth  = 1

class MentorDetialSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model  = Mentor
        fields = '__all__'
        depth  = 1

class MentorSignupSerializer(ModelSerializer):
    user = UserSignupSerializer()

    class Meta:
        model  = Mentor
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data.pop('user'), is_mentor=True)
        validated_data.pop('managedCourses')
        validated_data.pop('courseRequests')
        return Mentor.objects.create(user=user, **validated_data)

    def update(self, instance, validated_data):
        try:
            user                   = validated_data.pop('user')
            instance.user.username = user.get('username', instance.user.username)
            instance.user.email    = user.get('email', instance.user.email)
            instance.user.password = user.get('password', instance.user.password)
            instance.user.save()
        except KeyError:
            pass
        try:
            instance.managedCourses.set(validated_data.pop('managedCourses'))
        except KeyError:
            pass
        try:
            instance.courseRequests.set(validated_data.pop('courseRequests'))
        except KeyError:
            pass
        instance.save()
        return instance
