from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

# Create your models here.

class UserManager(BaseUserManager):

  def _create_user(self,is_headmaster,is_teacher,is_student,name,email, password,post,roll_no,Class, is_staff, is_superuser, **extra_fields):
    if not email:
        raise ValueError('Users must have an email address')
    now = timezone.now()
    email = self.normalize_email(email)
    user = self.model(is_headmaster=is_headmaster,is_teacher=is_teacher,is_student=is_student,
        name=name,
        email=email,
        post=post,
        roll_no=roll_no,
        Class=Class,
        is_staff=is_staff,
        is_active=True,
        is_superuser=is_superuser,
        last_login=now,
        date_joined=now,
        **extra_fields
    )
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self,is_headmaster,is_teacher,is_student,name, email, password,post,roll_no,Class, **extra_fields):
    return self._create_user(is_headmaster,is_teacher,is_student,name,email, password, post,roll_no,Class,**extra_fields)

  def create_superuser(self,name, email, password, **extra_fields):
    user=self._create_user(False,False,False,name,email, password, True, True, **extra_fields)
    return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    post = models.CharField(max_length=254, null=True, blank=True)
    roll_no=models.CharField(max_length=254, null=True, blank=True)
    Class=models.IntegerField(null=True, blank=True)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    is_headmaster=models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = UserManager()



class Teachers_class_lecture(models.Model):
     teacher=models.ForeignKey(User, related_name='tclass' ,on_delete=models.CASCADE)
     class_t=models.IntegerField()
     lecture=models.CharField(max_length=20)
     start_time=models.TimeField(null=True, blank=True)
     end_time=models.TimeField(null=True, blank=True)

class Student_task_assign(models.Model):
    teacher=models.ForeignKey(User,related_name='S_task_a',on_delete=models.CASCADE,null=True,blank=True)
    class_s=models.IntegerField()
    description=models.TextField(null=True,blank=True)
    pdf= models.FileField(upload_to='tasks/pdf/',null=True,blank=True)
    submission_date=models.DateField(null=True,blank=True)
    total_marks=models.IntegerField(null=True,blank=True)


class Student_task_result(models.Model):
    student_id=models.ForeignKey(User,related_name='result_sid',on_delete=models.CASCADE,null=True,blank=True)
    task_id=models.ForeignKey(Student_task_assign,related_name='result_tid',on_delete=models.CASCADE,null=True,blank=True)
    marks=models.IntegerField(null=True,blank=True)
    status=models.CharField(max_length=20, null=True, blank=True)
    result=models.TextField(null=True,blank=True)
    resultp=models.FileField(upload_to='tasks/pdf/',null=True,blank=True)



class Sports_game(models.Model):
    Name=models.CharField(max_length=20)
    No_of_Players=models.IntegerField()
    Playing_hours=models.FloatField()


    Teacher_name=models.CharField(max_length=20)
