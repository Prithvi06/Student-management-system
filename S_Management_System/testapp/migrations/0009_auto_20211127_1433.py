# Generated by Django 3.1 on 2021-11-27 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0008_auto_20211127_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_task',
            name='sub_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
