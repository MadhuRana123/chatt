from pickle import TRUE
from django.db import models
from django.forms import IntegerField
from .models import*
from .managers import CustomManager

# Create your models here.
#####=========Chat applications===============

class Message(models.Model):
  user_name = models.CharField(max_length=255)
  room = models.CharField(max_length=255)
  content = models.TextField()
  date_added = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ('date_added',)

class Teacher(models.Model):  
    teacher_name = models.CharField(max_length=200)  
    active = models.BooleanField(default= False)
    archived = models.BooleanField(default=False)
  
    def __str__(self):  
        return f'{self.teacher_name}'  


class Student(models.Model):  
    username = models.CharField(max_length=20)  
    first_name = models.CharField(max_length=30)  
    last_name = models.CharField(max_length=30)  
    mobile = models.CharField(max_length=10)  
    email = models.EmailField()
    teacher_name = models.ForeignKey(Teacher, blank = True, null = True, on_delete= models.CASCADE,related_name= 'xyz')   
  
    def __str__(self):  
        return "%s %s" % (self.first_name, self.last_name)  


##### ==================Abstract  base class=========
class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    date = models.DateField()
    class Meta:
        abstract = True
class Sts(CommonInfo):
    fees = models.IntegerField()
    date = None

class Ts(CommonInfo):
    salary = models.IntegerField()

class Contractor(CommonInfo):
    date = models.DateTimeField()
    payment = models.IntegerField()
    
###### ==============multi tabel inheritance ============

class ExamCenter(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

class Semester(ExamCenter):
    sem_name = models.CharField(max_length=100)
    role = models.IntegerField()
   
### ===============proxy tabel inheritance===================

class UnvCenter(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

class MyUnvCenter(UnvCenter):
    class Meta:
        proxy = True



##### ==================MODEL MANAGER/custom manager model==============

class Sweet(models.Model):
    name = models.CharField(max_length=100)
    cls = models.IntegerField()
    sweets = CustomManager() ## custom manager----------------
    # objects = models.Manager() ##model manager----------