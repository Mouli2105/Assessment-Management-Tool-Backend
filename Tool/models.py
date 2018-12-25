from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_mentor  = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Course(models.Model):
    name        = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    arhived     = models.BooleanField()

    def __str__(self):
        return 'Course: ' + self.name

class Student(models.Model):
    user          = models.OneToOneField(User, on_delete=models.CASCADE)
    college       = models.CharField(max_length=100)
    branch        = models.CharField(max_length=10)
    section       = models.CharField(max_length=10)
    optedCourses  = models.ManyToManyField(Course, blank=True, related_name='students')
    registrations = models.ManyToManyField(Course, blank=True, related_name='studentRequests')

    def __str__(self):
        return 'Student: ' + self.user.username

class Mentor(models.Model):
    user           = models.OneToOneField(User, on_delete=models.CASCADE)
    managedCourses = models.ManyToManyField(Course, blank=True, related_name='mentors')
    courseRequests = models.ManyToManyField(Course, blank=True, related_name='mentorInvites')

    def __str__(self):
        return 'Mentor: ' + self.user.username

class Task(models.Model):
    course    = models.ForeignKey(Course, on_delete=models.CASCADE)
    No        = models.IntegerField()
    title     = models.CharField(max_length=100)
    content   = models.CharField(blank=True, null=True, max_length=500)
    questions = models.FileField(blank=True, null=True)

    def __str__(self):
        return 'Task: ' + self.title[:4] + '...'

class Submission(models.Model):
    course     = models.ForeignKey(Course, on_delete=models.CASCADE)
    task       = models.ForeignKey(Task, on_delete=models.CASCADE)
    student    = models.ForeignKey(Student, on_delete=models.CASCADE)
    submission = models.FileField()
    
    def __str__(self):
        return 'Submission in ' + self.course.__str__() + ' by ' + self.student.__str__()