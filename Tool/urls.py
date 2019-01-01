from django.urls import path
from Tool.views import *
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

app_name = 'assessment_tool'

urlpatterns = [
    # COURSE VIEWS
    path('courses/', ListSearchedCourses.as_view(), name='course-search'),
    path('courses/<int:c_id>/', DetailCourse.as_view(), name='course-detail'),
    path('courses/<int:c_id>/tasks/', ListTasksOfCourse.as_view(), name='course-task-list'),
    path('courses/<int:c_id>/tasks/<int:t_id>/', DetailTaskOfCourse.as_view(), name='course-task-detail'),
    path('courses/<int:c_id>/tasks/<int:t_id>/submissions/', ListSubmissionsOfTask.as_view(), name='task-submission-list'),
    path('courses/<int:c_id>/tasks/<int:t_id>/submissions/<int:sub_id>/', DetailSubmissionOfTask.as_view(), name='task-submission-detail'),
    path('courses/<int:c_id>/students/', ListStudentsOfCourse.as_view(), name='course-student-list'),
    path('courses/<int:c_id>/students/<int:s_id>/', DetailStudentOfCourse.as_view(), name='course-student-detail'),
    path('courses/<int:c_id>/mentors/', ListMentorsOfCourse.as_view(), name='course-mentor-list'),
    path('courses/<int:c_id>/mentors/<int:m_id>/', DetailMentorOfCourse.as_view(), name='course-mentor-detail'),
    path('courses/<int:c_id>/registrations/', ListCourseRegistrations.as_view(), name='course-registration-list'),

    # STUDENT VIEWS
    path('students/', ListSearchedStudents.as_view(), name='student-search'),
    path('students/<int:s_id>/', DetailStudent.as_view(), name='student-detail'),
    
    # MENTOR VIEWS
    path('mentors/', ListSearchedMentors.as_view(), name='mentor-search'),
    path('mentors/<int:m_id>/', DetailMentor.as_view(), name='mentor-detail'),

    # AUTH VIEWS
    path('auth/token/', obtain_jwt_token),
    path('auth/token/refresh/', refresh_jwt_token),

]