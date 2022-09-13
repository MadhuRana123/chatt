from telnetlib import SE
from django.shortcuts import render
from .models import Message
from django.http import HttpResponse
from .models import*
from .models import Student as Students
from django.db.models import Q
from .models import*


# Create your views here.
def index(request):
  return render(request, 'index.html')


def room(request, room_name):
  username = request.GET.get('username', 'Anonymous')
  messages = Message.objects.filter(room=room_name)[0:25]
  return render(request, 'room.html', {'room_name': room_name, 'username': username,'messages': messages})


def student(request):
  print('7777777777777777')
  stu_all = Students.objects.all()
  print('1==============',[stu_all.first_name for stu_all in stu_all ])
  stu_queryset = Students.objects.exclude(first_name__startswith = 'm')
  print('2===========',stu_queryset)
  return HttpResponse('here')


def teacher_name(request):
  queryset = Student.objects.filter(first_name__startswith='m') & Student.objects.filter(last_name__startswith='r')
  print('a============',queryset)
  #  queryset = Student.objects.filter(Q(first_name__startswith='a') & Q(last_name__startswith='c'))
  #  print(queryset)
  queryset_new =Student.objects.filter(
    Q(first_name__startswith='a') | ~Q(last_name__startswith='c'))
  print(queryset)

  # queryset = Student.objects.filter(
  # Q(first_name__startswith='a') & ~Q(last_name__startswith='c'))
  print('queryset_new---------------',queryset_new)
  # stu=Teacher.objects.prefetch_related('xyz')
  # for i in stu:
  #   print(i.xyz.all())
  
  # stu = Student.objects.all().select_related('teacher_name')
  # stu =Student.objects.select_related('teacher_name').filter(teacher_name__active=True, teacher_name__archived=False)
  # print(stu)
  
  # for i in stu:
  # #   print('hii')
  #  print(i.teacher_name.teacher_name)
  return HttpResponse('here')

def home(request):
  context = {}
  sts_data = Sts.objects.all()
  ts_data = Ts.objects.all()
  Contractor_data = Contractor.objects.all()
  exam_center = ExamCenter.objects.all()
  semester = Semester.objects.all()
  # sweet = Sweet.objects.all() ## model manager---------------
  sweet = Sweet.sweets.all()  ##custom manager----------------------
  context = {'stss':sts_data,'tss':ts_data,'contractors':Contractor_data, 'centers':exam_center,'semesters': semester,'sweets':sweet}
  return render (request,'home.html',context)




#---------------------- function middleware view-----------------

def function_based(request):
  print("i am view")
  return HttpResponse("this is home page")

#---------------class middleware view-----------

def class_based(request):
  print("i am view")
  return HttpResponse("this is home page")


def Custom_Middleware(request):
  print("hello")
  return HttpResponse("this is custom page")