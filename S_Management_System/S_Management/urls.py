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
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from testapp import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    url('admin/', admin.site.urls),
    #url(r'^$',views.Admin_panel_view,name='admin_panel'),
    url(r'^logout/', auth_views.LogoutView.as_view(template_name= 'registration/logged_out.html',next_page=None), name='logout'),
    url(r'^login/', views.Login_view, name='login'),
    url(r'^Mheadmaster/$',views.Headmaster_manage_view,name='Mheadmaster'),   #manage headmaster
    url(r'^Rheadmaster/$',views.Headmaster_register,name='Rheadmaster'),       #register headmaster
    url(r'^Rteacher/$',views.Teacher_register,name='Rteacher'),             #register teacher
    url(r'^Rstudent/$',views.Student_register,name='Rstudent'),              #register teacher
    url(r'^Mteacher/$',views.Teacher_manage_view,name='Mteacher'),  #manage teacher
    url(r'^Mstudent/$',views.Student_manage_view,name='Mstudent'),  #manage student
    url(r'^Mclassl/$',views.Manage_tclass_lecture,name='Mclassl'),    #manage t_class
    url(r'^Aclass/$',views.Assign_class,name='Aclass'),                 #add class
    url(r'^gclass/(?P<id>\d+)/$',views.get_class_view,name='gclass'),   #get class Detail
    url(r'^tassign/$',views.Task_assign,name='tassign'),
    url(r'^taskv/$',views.Task_assign_view,name='taskv'),
    url(r'^tsk_Pstatus_assign/(?P<id1>\d+)/(?P<id2>\d+)/$',views.Student_task_Presult_view,name='tsk_Pstatus_assign'),
    url(r'^tsk_Cstatus_assign/(?P<id1>\d+)/(?P<id2>\d+)/$',views.Student_task_Cresult_view,name='tsk_Cstatus_assign'),
    url(r'^tsk_detail/(?P<id>\d+)/$',views.Task_status_detail,name='tsk_detail'),
    url(r'^gmarks/(?P<id1>\d+)/(?P<id2>\d+)/$',views.give_marks,name='gmarks'),

    url(r'^Asports/$',views.Sports_class,name='Add_sports'),         #add sports
    url(r'^Msports/$',views.Manage_sports_view,name='Msports'),     #manage sports view
    url(r'^hupdate/(?P<id>\d+)/$',views.hupdate_view,name='hupdate'),
    url(r'^tupdate/(?P<id>\d+)/$',views.tupdate_view,name='tupdate'),
    url(r'^supdate/(?P<id>\d+)/$',views.supdate_view,name='supdate'),
    url(r'^cupdate/(?P<id>\d+)/$',views.cupdate_view,name='update'),
    url(r'^department/$',views.department_view,name='department'),
    url(r'^delete/(?P<id>\d+)/$',views.delete_view,name='delete'),
    url(r'^cdelete/(?P<id>\d+)/$',views.cdelete_view,name='cdelete'),

    url(r'^head_profile/$',views.head_profile_view,name='head_profile'),
    url(r'^teacher_profile/$',views.teacher_profile_view,name='teacher_profile'),
    url(r'^teacher_lecture/$',views.teacher_lecture_view,name='teacher_lecture'),
    url(r'^student_profile/$',views.student_profile_view,name='student_profile'),
    url(r'^student_lecture/$',views.student_lecture_view,name='student_lecture'),


    url('reset_password/', auth_views.PasswordResetView.as_view(),name="reset_password"),
    url('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
