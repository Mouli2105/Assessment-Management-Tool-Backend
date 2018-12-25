from django.contrib import admin
from Tool.models import *

admin.site.register(User)
admin.site.register(Mentor)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Task)
admin.site.register(Submission)