# Generated by Django 3.1 on 2021-11-28 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0011_auto_20211127_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='marks',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.DeleteModel(
            name='Student_task_result',
        ),
    ]
