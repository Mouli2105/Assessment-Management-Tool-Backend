from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    college = models.CharField(max_length=100)
    branch = models.CharField(max_length=10)
    section = models.CharField(max_length=10)

    def __str__(self):
        return 'Student: ' + self.user.username

class Mentor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return 'Mentor: ' + self.user.username

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    students = models.ManyToManyField(Student, blank=True)
    mentors = models.ManyToManyField(Mentor, blank=True)

    def __str__(self):
        return 'Course: ' + self.name

class Task(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    No = models.IntegerField()
    title = models.CharField(max_length=100)
    content = models.CharField(blank=True, null=True, max_length=500)
    questions = models.FileField(blank=True, null=True)

    def __str__(self):
        return 'Task: ' + self.title[:4] + '...'

class Submission(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    submission = models.FileField()
    
    def __str__(self):
        return 'Submission in ' + self.course + ' by ' + self.student

