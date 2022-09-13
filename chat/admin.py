from django.contrib import admin

from chat.views import Teacher,Student,Sts,Ts,Contractor,ExamCenter,Semester, UnvCenter,MyUnvCenter,Sweet

# Register your models here.
from .models import *

admin.site.register(Message)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Sts)
admin.site.register(Ts)
admin.site.register(Contractor)
admin.site.register(ExamCenter)
admin.site.register(Semester)
admin.site.register(UnvCenter)
admin.site.register(MyUnvCenter)
admin.site.register(Sweet)