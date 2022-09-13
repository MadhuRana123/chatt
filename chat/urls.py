from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  # path('<str:room_name>/', views.room, name='room'),
  path('student/', views.student, name='student'),
  path('teacher_name/', views.teacher_name, name='teacher_name'),
  path('home/',views.home,name='home'),
  path('function_based/',views.function_based,name='function_based'),
  path('class_based/',views.class_based,name='class_based'),
  path('Custom_Middleware/',views.Custom_Middleware,name='Custom_Middleware')
    

]