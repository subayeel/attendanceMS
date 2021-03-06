from django.urls import path
from . import views

urlpatterns = [
    path('allstudents/', views.student_list, name='student_list'),
    path('<int:student_id>/', views.single_student, name='single_student'),
    path('registration/', views.student_regi, name='student_regi'),
    path('edit/<int:pk>', views.edit_student, name='edit_student'),
    path('delete/<int:student_id>', views.delete_student, name='delete_student'),
    path('attendance/count/', views.attendance_count, name='attendance_count'),

    #take attendance button urls
    path('takeattendance/sub1/<student_id>',views.take_sub1_att,name='take_sub1_att'),
    path('takeattendance/sub2/<student_id>',views.take_sub2_att,name='take_sub2_att'),
    path('takeattendance/sub3/<student_id>',views.take_sub3_att,name='take_sub3_att'),
    path('takeattendance/sub4/<student_id>',views.take_sub4_att,name='take_sub4_att'),
    path('takeattendance/sub5/<student_id>',views.take_sub5_att,name='take_sub5_att'),
    path('takeattendance/sub6/<student_id>',views.take_sub6_att,name='take_sub6_att'),
    path('takeattendance/lab1/<student_id>',views.take_lab1_att,name='take_lab1_att'),
    path('takeattendance/lab2/<student_id>',views.take_lab2_att,name='take_lab2_att'),

    #attendance of each subject
    path('sub1/<student_id>',views.increase_sub1_att,name='increase_sub1_att'),
    path('sub2/<student_id>',views.increase_sub2_att,name='increase_sub2_att'),
    path('sub3/<student_id>',views.increase_sub3_att,name='increase_sub3_att'),
    path('sub4/<student_id>',views.increase_sub4_att,name='increase_sub4_att'),
    path('sub5/<student_id>',views.increase_sub5_att,name='increase_sub5_att'),
    path('sub6/<student_id>',views.increase_sub6_att,name='increase_sub6_att'),
    path('lab1/<student_id>',views.increase_lab1_att,name='increase_lab1_att'),
    path('lab2/<student_id>',views.increase_lab2_att,name='increase_lab2_att'),

    #cancel the class
    path('sub1/cancel/<sub>',views.cancel_sub1_att,name='cancel_sub1_att'),
    path('sub2/cancel/<sub>',views.cancel_sub2_att,name='cancel_sub2_att'),
    path('sub3/cancel/<sub>',views.cancel_sub3_att,name='cancel_sub3_att'),
    path('sub4/cancel/<sub>',views.cancel_sub4_att,name='cancel_sub4_att'),
    path('sub5/cancel/<sub>',views.cancel_sub5_att,name='cancel_sub5_att'),
    path('sub6/cancel/<sub>',views.cancel_sub6_att,name='cancel_sub6_att'),
    path('lab1/cancel/<sub>',views.cancel_lab1_att,name='cancel_lab1_att'),
    path('lab2/cancel/<sub>',views.cancel_lab2_att,name='cancel_lab2_att'),

    #increment extra class counter
    path('sub1/extraclass/<student_id>',views.extra_class_sub1,name='extra_class_sub1'),
    path('sub2/extraclass/<student_id>',views.extra_class_sub2,name='extra_class_sub2'),
    path('sub3/extraclass/<student_id>',views.extra_class_sub3,name='extra_class_sub3'),
    path('sub4/extraclass/<student_id>',views.extra_class_sub4,name='extra_class_sub4'),
    path('sub5/extraclass/<student_id>',views.extra_class_sub5,name='extra_class_sub5'),
    path('sub6/extraclass/<student_id>',views.extra_class_sub6,name='extra_class_sub6'),
    path('lab1/extraclass/<student_id>',views.extra_class_lab1,name='extra_class_lab1'),
    path('lab2/extraclass/<student_id>',views.extra_class_lab2,name='extra_class_lab2'),

    #urls for semesters
    path('semester/registration/', views.sem_register, name='sem_register'),
    path('allsemesters/', views.sem_list, name='sem_list'),
    path('edit/semester/<int:sem_number>', views.edit_sem, name='edit_sem'),
    path('delete/semester/<int:sem_number>', views.delete_sem, name='delete_sem'),

    path('subject/registration/', views.create_subject, name='create_subject'),
    path('allsubject/', views.subject_list, name='subject_list'),
    path('<slug:subject_code>/', views.single_subject, name='single_subject'),
    path('edit/<slug:pk>', views.edit_subject, name='edit_subject'),
    path('delete/<slug:subject_code>', views.delete_subject, name='delete_subject'),
    
    
    
]

