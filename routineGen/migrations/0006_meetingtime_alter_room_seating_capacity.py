# Generated by Django 4.0.3 on 2022-03-29 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routineGen', '0005_delete_meetingtime_alter_course_credit_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeetingTime',
            fields=[
                ('meeting_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('meeting_day', models.CharField(max_length=11)),
                ('meeting_time', models.TimeField()),
            ],
            options={
                'verbose_name': 'Meeting Time',
                'db_table': 'meetingtime',
            },
        ),
        migrations.AlterField(
            model_name='room',
            name='seating_capacity',
            field=models.IntegerField(),
        ),
    ]