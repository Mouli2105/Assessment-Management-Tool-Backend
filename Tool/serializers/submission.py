from rest_framework.serializers import ModelSerializer
from Tool.models import *

class SubmissionSerializer(ModelSerializer):
    class Meta:
        model  = Submission
        fields = '__all__'