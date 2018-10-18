from django.urls import path
from Tool.views import *

app_name = 'assessment_tool'

urlpatterns = [
    path('courses/', ListCourses.as_view(), name='all-courses')
]