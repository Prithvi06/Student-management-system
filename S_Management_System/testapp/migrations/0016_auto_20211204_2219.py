# Generated by Django 3.1 on 2021-12-04 16:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0015_auto_20211130_1130'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Teachers_class',
            new_name='Teachers_class_lecture',
        ),
        migrations.RemoveField(
            model_name='student_task_assign',
            name='Class',
        ),
        migrations.AddField(
            model_name='student_task_assign',
            name='std_task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='S_task_a', to='testapp.teachers_class_lecture'),
        ),
        migrations.AlterField(
            model_name='student_task_result',
            name='student_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='result_sid', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='student_task_result',
            name='task_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='result_tid', to='testapp.student_task_assign'),
        ),
    ]
