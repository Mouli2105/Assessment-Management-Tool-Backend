from rest_framework.serializers import ModelSerializer
from Tool.models import *
from Tool.serializers.user import UserSerializer, UserSignupSerializer

class StudentSerializer(ModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model  = Student
        fields = ('id', 'user', 'college', 'branch', 'section')
        depth  = 1

class StudentDetailSerializer(ModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model  = Student
        fields = '__all__'
        depth  = 1

class StudentSignupSerializer(ModelSerializer):
    user = UserSignupSerializer()
    
    class Meta:
        model  = Student
        fields = '__all__'

    def create(self, validated_data):
        user = User.objects.create(**validated_data.pop('user'), is_student=True)
        validated_data.pop('optedCourses')

        validated_data.pop('registrations')
        return Student.objects.create(user=user, **validated_data)

    def update(self, instance, validated_data):
        try:
            user                   = validated_data.pop('user')
            instance.user.username = user.get('username', instance.user.username)
            instance.user.email    = user.get('email', instance.user.email)
            instance.user.password = user.get('password', instance.user.password)      
            instance.user.save()
        except KeyError:
            pass
        instance.college = validated_data.get('college', instance.college)
        instance.branch  = validated_data.get('branch', instance.branch)
        instance.section = validated_data.get('section', instance.section)
        try:
            instance.optedCourses.set(validated_data.pop('optedCourses'))
        except:
            pass
        try:
            instance.registrations.set(validated_data.pop('registrations'))
        except:
            pass
        instance.save()
        return instance