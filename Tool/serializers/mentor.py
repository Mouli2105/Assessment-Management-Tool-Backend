from rest_framework.serializers import ModelSerializer
from Tool.models import *
from Tool.serializers.user import UserSerializer

class MentorSerializer(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Mentor
        fields = '__all__'