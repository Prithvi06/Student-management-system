from django import forms
from testapp.models import Teachers_class_lecture,Sports_game,Student_task_assign
class LoginForm(forms.Form):
    email = forms.EmailField(label="email")
    password = forms.CharField(label="Password",widget=forms.PasswordInput)


class Assign_classForm(forms.ModelForm):
    class Meta:
        model=Teachers_class_lecture
        fields='__all__'

class Student_task_assign_Form(forms.ModelForm):
    class Meta:
        model=Student_task_assign
        fields='__all__'

class Sports_gameForm(forms.ModelForm):
    class Meta:
        model=Sports_game
        fields='__all__'
