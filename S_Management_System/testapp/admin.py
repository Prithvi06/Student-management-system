from django.contrib import admin

# Register your models here.
from .models import User,Teachers_class_lecture,Sports_game,Student_task_assign,Student_task_result

class UserAdmin(admin.ModelAdmin):
    list_display = ('name','email','password')
admin.site.register(User,UserAdmin)


admin.site.register(Teachers_class_lecture)
admin.site.register(Sports_game)
admin.site.register(Student_task_assign)
admin.site.register(Student_task_result)
