"""S_Management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from testapp import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('$',views.Admin_panel_view,name='admin_panel'),
    path('logout/', auth_views.LogoutView.as_view(template_name= 'registration/logged_out.html',next_page=None), name='logout'),
    path('login/', views.Login_view, name='login'),
    path('Mheadmaster/',views.Headmaster_manage_view,name='Mheadmaster'),   #manage headmaster
    path('Rheadmaster/',views.Headmaster_register,name='Rheadmaster'),       #register headmaster
    path('Rteacher/',views.Teacher_register,name='Rteacher'),             #register teacher
    path('Rstudent/',views.Student_register,name='Rstudent'),              #register teacher
    path('Mteacher/',views.Teacher_manage_view,name='Mteacher'),  #manage teacher
    path('Mstudent/',views.Student_manage_view,name='Mstudent'),  #manage student
    path('Mclassl/',views.Manage_tclass_lecture,name='Mclassl'),    #manage t_class
    path('Aclass/',views.Assign_class,name='Aclass'),                 #add class
    path('gclass/<int:id>',views.get_class_view,name='gclass'),   #get class Detail
    path('tassign/',views.Task_assign,name='tassign'),
    path('taskv/',views.Task_assign_view,name='taskv'),
    path('tsk_Pstatus_assign/<int:id1>/<int:id2>/',views.Student_task_Presult_view,name='tsk_Pstatus_assign'),
    path('tsk_Cstatus_assign/<int:id1>/<int:id2>/$',views.Student_task_Cresult_view,name='tsk_Cstatus_assign'),
    path('tsk_detail/<int:id>',views.Task_status_detail,name='tsk_detail'),
    path('gmarks/<int:id1>/<int:id2>/',views.give_marks,name='gmarks'),

    path('Asports/',views.Sports_class,name='Add_sports'),         #add sports
    path('Msports/',views.Manage_sports_view,name='Msports'),     #manage sports view
    path('hupdate/<int:id>/',views.hupdate_view,name='hupdate'),
    path('tupdate/<int:id>/',views.tupdate_view,name='tupdate'),
    path('supdate/<int:id>/',views.supdate_view,name='supdate'),
    path('cupdate/<int:id>/',views.cupdate_view,name='update'),
    path('department/',views.department_view,name='department'),
    path('delete/<int:id>/',views.delete_view,name='delete'),
    path('cdelete/<int:id>/',views.cdelete_view,name='cdelete'),

    path('head_profile/',views.head_profile_view,name='head_profile'),
    path('teacher_profile/',views.teacher_profile_view,name='teacher_profile'),
    path('teacher_lecture/',views.teacher_lecture_view,name='teacher_lecture'),
    path('student_profile/',views.student_profile_view,name='student_profile'),
    path('student_lecture/',views.student_lecture_view,name='student_lecture'),


    path('reset_password/', auth_views.PasswordResetView.as_view(),name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    path('reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
