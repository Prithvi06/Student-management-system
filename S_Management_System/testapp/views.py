from django.shortcuts import render,redirect
from .models import User,Sports_game,Teachers_class_lecture,Student_task_assign,Student_task_result
from testapp.forms import LoginForm,Assign_classForm,Sports_gameForm,Student_task_assign_Form
from django.contrib.auth import authenticate,login
from django.contrib import messages
# Create your views here.


scount=User.objects.filter(is_student=True).count()
tcount=User.objects.filter(is_teacher=True).count()
tsports=Sports_game.objects.all().count()
print(scount,tcount,tsports)
def Headmaster_register(request):
    """ Headmaster Registration  function"""
    if (request.method == 'POST'):
                name = request.POST.get('name')
                email = request.POST.get('email')
                password = request.POST.get('password')
                user = User.objects.create_user(is_headmaster=True,name=name,email=email ,password=password)
                user.set_password(password)
                user.save()
                print('Headmaster created Successsfuly')
                messages.success(request,'Headmaster Successsfuly Created !!!')
                return render(request,'testapp/admin_panel.html',{'success':True,'super':True,'login':False,})

    return render(request, 'testapp/register.html',{'super':True})

def Teacher_register(request):
    """ Teacher Registration  function"""
    if request.user.is_authenticated and (request.user.is_superuser or request.user.is_headmaster):
        super=request.user.is_superuser
        head=request.user.is_headmaster
        if (request.method == 'POST'):
                    name = request.POST.get('name')
                    email = request.POST.get('email')
                    password = request.POST.get('password')
                    post=request.POST.get('post')
                    user = User.objects.create_user(is_headmaster=False,is_teacher=True,is_student=False,name=name,email=email ,password=password ,post=post)
                    user.set_password(password)
                    user.save()
                    print('Teacher created Successsfuly')
                    messages.success(request,'teacher Successsfuly Created !!!')
                    return render(request,'testapp/admin_panel.html',{'success':True,'super':super,'head':head})
        return render(request, 'testapp/tregister.html',{'super':super,'head':head})

def Student_register(request):
    """ Student Registration  function"""
    if request.user.is_authenticated and (request.user.is_superuser or request.user.is_headmaster):
        super=request.user.is_superuser
        head=request.user.is_headmaster
        if (request.method == 'POST'):
                    name = request.POST.get('name')
                    email = request.POST.get('email')
                    password = request.POST.get('password')
                    roll_no=request.POST.get('roll_no')
                    Class=request.POST.get('Class')

                    user = User.objects.create_user(is_headmaster=False,is_teacher=False,is_student=True,name=name,email=email ,password=password ,roll_no=roll_no,Class=Class,)
                    user.set_password(password)
                    user.save()
                    print('Student created Successsfuly')
                    messages.success(request,'Student Successsfuly Created !!!')
                    return render(request,'testapp/admin_panel.html',{'success':True,'super':super,'head':head})
        return render(request, 'testapp/sregister.html',{'super':super,'head':head})


def Login_view(request):
        super=False
        head=False
        form=LoginForm()
        if (request.method=='POST'):
                print('post')
                email = request.POST.get('email') #Get email value from form
                password = request.POST.get('password') #Get password value from form
                user = authenticate(request, email=email, password=password)
                if user is not None:
                        login(request, user)
                        print('authenticate')
                        if user.is_authenticated and request.user.is_superuser:
                            super=request.user.is_superuser
                            print('superuser Login')
                            return render(request,'testapp/admin_panel.html',{'super':super,'login':False,})


                        if user.is_authenticated and request.user.is_headmaster:
                            print('headmaster Login')
                            head=request.user.is_headmaster
                            return render(request,'testapp/admin_panel.html',{'head':head,'login':False,})

                        if user.is_authenticated and request.user.is_teacher:
                                teacher=request.user.is_teacher
                                print('teacher login view')
                                return render(request,'testapp/admin_panel.html',{'teacher':teacher,'login':False,})


                        if user.is_authenticated and request.user.is_student:
                                student=request.user.is_student
                                print('student login view')
                                return render(request,'testapp/admin_panel.html',{'student':student,'login':False,})

                else:
                    print("user is not authenticated")
                    messages.error(request,'username or password not correct')
                    return redirect('login')

        if request.user.is_authenticated and request.user.is_superuser:
              super=request.user.is_superuser
              print('already superuser authenticate')
              return render(request,'testapp/admin_panel.html',{'super':super,'login':False})

        elif request.user.is_authenticated and request.user.is_headmaster:
              head=request.user.is_headmaster
              print('already headmaster authenticate')
              return render(request,'testapp/admin_panel.html',{'head':head,'login':False})

        elif request.user.is_authenticated and request.user.is_teacher:
              teacher=request.user.is_teacher
              print('already teacher authenticate')
              return render(request,'testapp/admin_panel.html',{'teacher':teacher,'login':False})

        elif request.user.is_authenticated and request.user.is_student:
                student=request.user.is_student
                print('already student authenticate')
                return render(request,'testapp/admin_panel.html',{'student':student,'login':False})


        return render(request,'testapp/login.html',{'form':form})


def head_profile_view(request):
    """ Headmaster profile function"""
    if request.user.is_authenticated and request.user.is_headmaster:
        head_data=User.objects.get(id=request.user.id)

        print(head_data)
        return render(request,'testapp/admin_panel.html',{"head_data":head_data,'login':False,'head_profile':request.user.is_headmaster,'head':request.user.is_headmaster})


def teacher_profile_view(request):
    """ Teacher profile function"""
    if request.user.is_authenticated and request.user.is_teacher:
        teacher_data=User.objects.get(id=request.user.id)
        print(teacher_data)
        return render(request,'testapp/admin_panel.html',{"teacher_data":teacher_data,'login':False,'teacher_profile':request.user.is_teacher,'teacher':request.user.is_teacher})


def teacher_lecture_view(request):
    """ Teacher Own lecture view function """
    if request.user.is_authenticated and request.user.is_teacher:
        teacher_class=User.objects.get(id=request.user.id)
        tclass_data=teacher_class.tclass.all()

        print(' teacher class views',teacher_class.tclass.all())
        return render(request,'testapp/admin_panel.html',{"tclass_data":tclass_data,'login':False,'teacher_class':request.user.is_teacher,'teacher':request.user.is_teacher})


def student_profile_view(request):
    """ Student profile function"""
    if request.user.is_authenticated and request.user.is_student:
        student_data=User.objects.get(id=request.user.id)

        print(student_data)
        return render(request,'testapp/admin_panel.html',{"student_data":student_data,'login':False,'student_profile':request.user.is_student,'student':request.user.is_student})

def student_lecture_view(request):
        """ Student can see Own lecture  function """
        if request.user.is_authenticated and request.user.is_student:
            student=request.user.is_student
            student_data=User.objects.get(id=request.user.id)
            print('student class',student_data.Class)

            teacher_data=User.objects.filter(is_teacher=True)
            teacher_list_id=[]
            for teacher in teacher_data:
                teacher_list_id.append(teacher.id)
            print(teacher_list_id)

            Classl_details={}
            sub={}
            i=1
            for id in teacher_list_id:
                teacher_data=User.objects.get(id=id)
                tclass_data=teacher_data.tclass.all()

                for tclass in tclass_data:
                    sub={}
                    if int(student_data.Class) == int(tclass.class_t):
                        sub['Class']=tclass.class_t# sub.append(tclass.Class)
                        sub['Lecture']=tclass.lecture# sub.append(tclass.Lecture)
                        sub['Teacher']=tclass.teacher.name# sub.append(tclass.Teacher)
                        sub['Start_time']=tclass.start_time
                        sub['End_time']=tclass.end_time
                        print(tclass.class_t,tclass.lecture)

                        Classl_details[i]=sub
                        i+=1
            print(Classl_details)
            return render(request,'testapp/admin_panel.html',{"Classl_details":Classl_details,'login':False,'student_lecture':student,'student':student})




def Assign_class(request):
    """ Admin or Headmaster Assign class and Lectures to Teacher """
    if request.user.is_authenticated and (request.user.is_superuser or request.user.is_headmaster):
        super=request.user.is_superuser
        head=request.user.is_headmaster
        form = Assign_classForm()
        if request.method == 'POST':
            form = Assign_classForm(request.POST)
            print('assignment form')
            if form.is_valid():
                print('submit')
                user = form.save()
                messages.success(request,'Class Given Successsfuly  !!!')
                return render(request,'testapp/admin_panel.html',{'success':True,'super':super,'head':head})

        return render(request, 'testapp/class_Assignment.html', {'form': form,'super':super,'head':head})



def get_class_view(request,id):
        """ Admin or Headmaster can view clasess and Lectures of each Teacher """
        print('get_class',id,request.user.id)
        print(type(id),type(request.user.id))
        if request.user.is_authenticated  and (request.user.is_superuser or request.user.is_headmaster):
            super=request.user.is_superuser
            head=request.user.is_headmaster
            print('get class',request.user.id)
            user_data=User.objects.get(id=id)
            class_data=user_data.tclass.all()
            print(class_data)
            return render(request,'testapp/admin_panel.html',{"class_data":class_data,'scount':scount,'tcount':tcount,'login':False,'super':super,'super_get_class':super,'head_get_class':head,'head':head})



def Sports_class(request):
    """ Sports Data View Function Every user can view this data"""
    if request.user.is_authenticated and (request.user.is_superuser or request.user.is_headmaster):
        form = Sports_gameForm()
        if request.method == 'POST':
            form = Sports_gameForm(request.POST)
            print('sports game form')
            if form.is_valid():
                print('submit')
                user = form.save()
                messages.success(request,'Game Given Successsfuly  !!!')
                return render(request,'testapp/admin_panel.html',{'success':True})

        return render(request, 'testapp/sports_game.html', {'form': form,'super':request.user.is_superuser,'head':request.user.is_headmaster})

from django.core.mail import send_mail
import time
from S_Management.settings import EMAIL_HOST_USER
def Task_assign(request):
    """Teacher Assign Tasks Function"""
    if request.user.is_authenticated and request.user.is_teacher:
        teacher=request.user.is_teacher
        if request.method == 'POST':
                Class=request.POST.get('Class')
                print("##########", Class)
                description=request.POST.get('description')
                pdf=request.FILES.get('pdf',None)
                sub_date=request.POST.get('sub_date')
                t_marks=request.POST.get('t_marks')
                Task_assign=Student_task_assign.objects.create(teacher=User.objects.get(id=request.user.id),class_s=Class,description=description,pdf=pdf,submission_date=sub_date,total_marks=t_marks)
                Task_assign.save()
                print('task save')
                std_user=User.objects.filter(is_student=True)
                for std in std_user:
                    if int(std.Class) == int(request.POST.get('Class')):
                        print(std.email,std.Class)
                        #send_mail('Hello'+std.name,,EMAIL_HOST_USER,[std.email])
                        #time.sleep(3)
                messages.info(request,'Task Assign Successfully')
                return render(request,'testapp/admin_panel.html',{'success':True,'teacher':teacher})
        return render(request,'testapp/task_assign.html',{'teacher':teacher,'task_assign':True})

def Task_assign_view(request):
    """ Task Assign function , Student can view own task"""
    if request.user.is_authenticated and request.user.is_student:
        user=User.objects.get(id=request.user.id)
        t_data=Student_task_assign.objects.all()
        print('task_data',user.Class,request.user.id,t_data)
        taskr_data=Student_task_result.objects.filter(student_id=int(request.user.id))
        print('student task result',taskr_data)
        marks_list=[]
        status_list=[]
        for task in taskr_data:
            status_list.append(task.status)
            marks_list.append(task.marks)
        print('status_list,marks_list',status_list,marks_list)
        result_list=[]
        for task in taskr_data:
            if task.result:
                result_list.append(task.result)
            elif task.resultp:
                result_list.append(task.resultp)
        print('result_list',result_list)
        task_data={}
        i=1
        j=0
        results=True
        status=False
        for task in t_data:
            sub={}
            print
            if int(task.class_s)==int(user.Class):
                sub['id']=task.id
                sub['description']=task.description
                sub['pdf']=task.pdf
                sub['sub_date']=task.submission_date
                sub['t_marks']=task.total_marks
                if len(status_list)!=0:
                    status=True
                    sub['status']=status_list[0]
                    status_list.pop(0)
                if len(result_list)!=0:
                    results=False
                    status=False
                    sub['result']=result_list[0]
                    result_list.pop(0)
                else:
                    sub['result']= None
                    status=True

                if len(marks_list)!=0:
                    sub['marks']=marks_list[0]
                    marks_list.pop(0)
                else:
                    sub['marks']=0
                task_data[i]=sub
                i+=1
                j+=1
        print(task_data)
        if task_data:
            empty_task=False
        else:
            empty_task=True
        print(status)
        return render(request,'testapp/admin_panel.html',{'task_data':task_data,'id':request.user.id,'student':request.user.is_student,'student_task_view':task_data,'empty_task':empty_task,'results':results,'status':status})



def Student_task_Cresult_view(request,*args, **kwargs):
    """ Student Complete Task result views """
    if request.user.is_authenticated and request.user.is_student:
                 std_id = kwargs.get('id1', None)
                 task_id = kwargs.get('id2', None)
                 print(std_id,task_id)
                 student=request.user.is_student
                 try:
                     already_task=Student_task_result.objects.get(task_id=int(task_id),student_id=int(std_id))
                 except Student_task_result.DoesNotExist:
                     already_task=None
                 if request.method=='POST':
                     solution=request.POST.get('solution')
                     pdf=request.FILES.get('pdf1',None)
                     if already_task:
                         already_task.status='Complete'
                         already_task.marks=0
                         if solution:
                             already_task.result=solution
                             already_task.resultp=pdf
                         else:
                             already_task.resultp=pdf
                         already_task.save()
                         print('already_task Complete')
                         #return redirect('/taskv')
                         messages.info(request,'Task Complete Successfully')
                         return render(request,'testapp/admin_panel.html',{'success':True,'student':student})
                     else:
                         if solution:
                             Student_task_result.objects.create(student_id=User.objects.get(id=int(std_id)),task_id=Student_task_assign.objects.get(id=int(task_id)),marks=0,status='Complete',result=solution,resultp=None)
                         else:
                             Student_task_result.objects.create(student_id=User.objects.get(id=int(std_id)),task_id=Student_task_assign.objects.get(id=int(task_id)),marks=0,status='Complete',result=None,resultp=pdf)
                         print('task answere done')
                         messages.info(request,'Task Complete Successfully')
                         return render(request,'testapp/admin_panel.html',{'success':True,'student':student})
                 else:
                     return render(request,'testapp/task_assign.html',{'student':student,})

def Student_task_Presult_view(request,*args, **kwargs):
    """ Student Pending Task result views """
    if request.user.is_authenticated and request.user.is_student:
                 std_id = kwargs.get('id1', None)
                 task_id = kwargs.get('id2', None)
                 print(std_id,task_id)
                 student=request.user.is_student
                 try:
                     task=Student_task_result.objects.get(task_id=int(task_id),student_id=int(std_id))
                 except Student_task_result.DoesNotExist:
                     task=None
                 print('task',task)
                 if task:
                     task.status='Pending'
                     task.marks=0
                     task.result=None
                     task.resultp=None
                     task.save()
                     print('already task Pending')
                 else:
                    Student_task_result.objects.create(student_id=User.objects.get(id=int(std_id)),task_id=Student_task_assign.objects.get(id=int(task_id)),marks=0,status='Pending',result=None,resultp=None)
                    print('task answere Pending')
                 messages.info(request,'Task In Pending')
                 return render(request,'testapp/admin_panel.html',{'success':True,'student':student})

def Task_status_detail(request,id):
    """ Teacher can view Student Task Status Details  and  result """
    print('task status Detail')
    if request.user.is_authenticated and request.user.is_teacher:
            teacher=request.user.is_teacher
            task_assign_data = Student_task_assign.objects.all()
            print('task_assign_data',task_assign_data)
            student_class=User.objects.get(id=id).Class
            marks_list=[]
            for task_assign in task_assign_data:
                if int(task_assign.class_s) == int(student_class):
                    marks_list.append(task_assign.total_marks)
            print('marks_list',marks_list)

            tresult_data=Student_task_result.objects.all()
            print('tresult_data',tresult_data)
            empty_tsk_detail=False
            o_marks=1
            status=True
            if tresult_data:
                        tasks_data_result={}
                        i=1
                        j=0
                        for task in tresult_data:
                            sub={}
                            if str(task.student_id)==User.objects.get(id=id).email:
                                std_task=task.task_id
                                print('description',std_task)
                                if std_task.description:
                                    sub['description']=std_task.description
                                else:
                                    sub['pdf']=std_task.pdf
                                sub['status']=task.status
                                if task.status=='Pending':
                                    status=False
                                sub['o_marks']=task.marks
                                if task.marks == 0:
                                    o_marks=0
                                sub['t_marks']=marks_list[j]
                                sub['result']=task.result
                                sub['resultp']=task.resultp
                                sub['id']=int(task.id)
                                tasks_data_result[i]=sub
                                i+=1
                                j+=1
                        print('task rstatus Detail',tasks_data_result)
                        if not tasks_data_result:
                            empty_tsk_detail=True

            elif task_assign_data:
                print('task_assign_data')
                tasks_data_result={}
                i=1
                for task_assign in task_assign_data:
                    sub={}
                    if int(task_assign.class_s) == int(student_class):
                        if task_assign.description:
                            sub['description']=task_assign.description
                        else:
                            sub['pdf']=task_assign.pdf
                        sub['status']='No Response'
                        sub['o_marks']=0
                        o_marks=0
                        sub['t_marks']=task_assign.total_marks
                        sub['result']='Not Submitted'
                        sub['resultp']=False
                        tasks_data_result[i]=sub
                        i+=1
                        give_marks=False
                        print('task status Detail',tasks_data_result)
                        if not tasks_data_result:
                            empty_tsk_detail=True
            else:
                empty_tsk_detail=True
                print('empty_tsk_detail')
            return render(request,'testapp/admin_panel.html',{'tasks_data_result':tasks_data_result,'teacher':teacher,'id':id,'empty_tsk_detail':empty_tsk_detail,'o_marks':o_marks,'status':status})

def give_marks(request,*args,**kwargs):
        """ Teacher give marks to student"""
        if request.user.is_authenticated and request.user.is_teacher:
            teacher=request.user.is_teacher
            id1=kwargs['id1']
            id2=kwargs['id2']
            student_class=User.objects.get(id=id1).Class
            task_assign_data = Student_task_assign.objects.all()
            print('task_assign_data',task_assign_data)
            marks_list=[]
            for task_assign in task_assign_data:
                if int(task_assign.class_s) == int(student_class):
                    marks_list.append(task_assign.total_marks)
            print('marks_list',marks_list)
            tresult_data=Student_task_result.objects.all()
            tasks_data_result={}
            i=1
            j=0
            for task in tresult_data:
                sub={}
                if str(task.student_id)==User.objects.get(id=id1).email:
                    std_task=task.task_id
                    if std_task.description:
                        sub['description']=std_task.description
                    else:
                        sub['pdf']=std_task.pdf
                    sub['status']=task.status
                    sub['t_marks']=marks_list[j]
                    sub['o_marks']=task.marks
                    if int(task.marks) == 0:
                        o_marks=0
                        print('o_marks',o_marks)
                    sub['result']=task.result
                    sub['resultp']=task.resultp
                    sub['id']=int(task.id)
                    tasks_data_result[i]=sub
                    i+=1
                    j+=1
            if request.method=='POST':
                    tresult_data=Student_task_result.objects.get(id=int(id2))
                    print('task Result',tresult_data)
                    tresult_data.marks=request.POST.get('marks')
                    tresult_data.save()
                    print('give Marks save',)
                    messages.info(request,'Marks given Successfully')
                    return render(request,'testapp/admin_panel.html',{'success':True,'teacher':teacher})

            else:
                return render(request,'testapp/admin_panel.html',{'tasks_data_result':tasks_data_result,'id':int(id2),'login':False,'teacher':True,'mform':True,'give_marks':True,'o_marks':o_marks,'status':True})


def Headmaster_manage_view(request):
    """View all Registered Headmaster """
    if request.user.is_authenticated and (request.user.is_superuser or request.user.is_headmaster):
        super=request.user.is_superuser
        print('headmaster Manage view')
        head_data=User.objects.filter(is_headmaster=True)
        return render(request,'testapp/admin_panel.html',{"head_data":head_data,'scount':scount,'tcount':tcount,'login':False,'super':super,'super_head_view':True})


def Teacher_manage_view(request):
    """View all registered teacher"""
    if request.user.is_authenticated and (request.user.is_superuser or request.user.is_headmaster):
        super=request.user.is_superuser
        head=request.user.is_headmaster
        print('teacher Manage view')
        teacher_data=User.objects.filter(is_teacher=True)
        return render(request,'testapp/admin_panel.html',{"teacher_data":teacher_data,'scount':scount,'tcount':tcount,'login':False,'super':super,'super_teacher_view':super,'head_teacher_view':head,'head':head})


def Student_manage_view(request):
    """View all registered Student"""
    if request.user.is_authenticated and (request.user.is_superuser or request.user.is_headmaster or request.user.is_teacher):
        super=request.user.is_superuser
        head=request.user.is_headmaster
        teacher=request.user.is_teacher
        print('student Manage view')
        student_data=User.objects.filter(is_student=True)
        return render(request,'testapp/admin_panel.html',{"student_data":student_data,'scount':scount,'tcount':tcount,'login':False,'super':super,'super_student_view':super,'head_student_view':head,'head':head,'teacher_student_view':teacher,'teacher':teacher})


def Manage_tclass_lecture(request):
    """View all Teacher Classes and lecture"""
    if request.user.is_authenticated and (request.user.is_superuser or request.user.is_headmaster):
        print('manage teacher class')
        super=request.user.is_superuser
        head=request.user.is_headmaster
        teacher_class_data=User.objects.filter(is_teacher=True)
        return render(request,'testapp/admin_panel.html',{"teacher_class_data":teacher_class_data,'scount':scount,'tcount':tcount,'login':False,'super':super,'super_classl_view':super,'head_classl_view':head,'head':head})


def Manage_sports_view(request):
    """View all Sports Detail"""
    if request.user.is_authenticated and (request.user.is_superuser or request.user.is_headmaster or request.user.is_teacher or request.user.is_student):
        super=request.user.is_superuser
        head=request.user.is_headmaster
        teacher=request.user.is_teacher
        student=request.user.is_student
        sport_data=Sports_game.objects.all()
        return render(request,'testapp/admin_panel.html',{"sport_data":sport_data,'scount':scount,'tcount':tcount,'login':False,'super':super,'super_sports_view':super,'head_sports_view':head,'teacher_sports_view':teacher,'head':head,'teacher':teacher,'student_sports_view':student,'student':student})


def department_view(request):
    print('department')
    if request.user.is_authenticated and (request.user.is_superuser or request.user.is_headmaster):
        head=request.user.is_headmaster
        super=request.user.is_superuser
        return render(request,'testapp/admin_panel.html',{'login':False,'super':super,'head':head,'department':True})




def hupdate_view(request,id):
    """headmaster update views"""
    user=User.objects.get(id=id)
    if request.user.is_authenticated and  (request.user.is_superuser or request.user.is_headmaster):
        if request.method=='POST':
            user.name=request.POST.get('name')
            user.email=request.POST.get('email')
            password=request.POST.get('password')
            user.set_password(password)
            user.save()
            print(request.POST.get('password'))
            print('update',)
            messages.info(request,'Record Update Successsfuly')
            return render(request,'testapp/admin_panel.html',{'scount':scount,'tcount':tcount,'login':False,'success':True,'super':True,'head':True})

    return render(request,'testapp/update.html',{'user':user,'super':True})


def tupdate_view(request,id):
    """Teacher update views"""
    user=User.objects.get(id=id)
    if request.user.is_authenticated and (request.user.is_superuser or request.user.is_headmaster):
        head=request.user.is_headmaster
        super=request.user.is_superuser
        if request.method=='POST':
            user.name=request.POST.get('name')
            user.email=request.POST.get('email')
            password=request.POST.get('password')
            user.post=request.POST.get('post')
            user.set_password(password)
            user.save()
            print(request.POST.get('password'))
            print('tupdate',)
            messages.info(request,'Record Update Successsfuly')
            return render(request,'testapp/admin_panel.html',{'scount':scount,'tcount':tcount,'login':False,'success':True,'super':super,'head':head})

        return render(request,'testapp/tupdate.html',{'user':user,'super':super,'head':head})


def supdate_view(request,id):
    """Student update views"""
    user=User.objects.get(id=id)
    if request.user.is_authenticated and (request.user.is_superuser or request.user.is_headmaster):
        head=request.user.is_headmaster
        super=request.user.is_superuser
        if request.method=='POST':
            user.name=request.POST.get('name')
            user.roll_no=request.POST.get('roll_no')
            user.email=request.POST.get('email')
            password=request.POST.get('password')
            user.Class=request.POST.get('Class')

            user.set_password(password)
            user.save()
            print(request.POST.get('password'))
            print('supdate',)
            messages.info(request,'Record Update Successsfuly')
            return render(request,'testapp/admin_panel.html',{'scount':scount,'tcount':tcount,'login':False,'success':True,'super':super,'head':head})

        return render(request,'testapp/supdate.html',{'user':user,'super':super,'head':head})


def cupdate_view(request,id):
        """Class and lecture update views"""
        user=Teachers_class_lecture.objects.get(id=id)
        if request.user.is_authenticated and (request.user.is_superuser or request.user.is_headmaster):
            head=request.user.is_headmaster
            super=request.user.is_superuser
            if request.method=='POST':
                user.lecture=request.POST.get('lecture')
                user.class_t=request.POST.get('class_t')
                user.start_time=request.POST.get('start_time')
                user.end_time=request.POST.get('end_time')
                print(request.POST.get('password'))
                print('cupdate')
                user.save()
                messages.info(request,'Record Update Successsfuly')
                return render(request,'testapp/admin_panel.html',{'scount':scount,'tcount':tcount,'login':False,'success':True,'super':request.user.is_superuser,'head':request.user.is_headmaster})

            return render(request,'testapp/cupdate.html',{'user':user,'super':request.user.is_superuser,'head':request.user.is_headmaster})



def delete_view(request,id):
    """headmaster delete views"""
    if request.user.is_authenticated and (request.user.is_superuser or request.user.is_headmaster):
        head=request.user.is_headmaster
        super=request.user.is_superuser
        user=User.objects.get(id=id)
        user.delete()
        messages.info(request,'Record deleted Successsfuly')
        return render(request,'testapp/admin_panel.html',{'scount':scount,'tcount':tcount,'login':False,'success':True,'super':super,'head':head})


def cdelete_view(request,id):
        """Teacher class and lecture delete views"""
        if request.user.is_authenticated and (request.user.is_superuser or request.user.is_headmaster):
            head=request.user.is_headmaster
            super=request.user.is_superuser
            user=Teachers_class_lecture.objects.get(id=id)
            user.delete()
            messages.info(request,'Record deleted Successsfuly')
            return render(request,'testapp/admin_panel.html',{'scount':scount,'tcount':tcount,'login':False,'success':True,'super':super,'head':head})
