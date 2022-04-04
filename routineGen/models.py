from django.db import models

# Create your models here.

class Room(models.Model):
    number = models.CharField(max_length=6, primary_key=True)
    seating_capacity = models.IntegerField()

    class Meta:
        ordering = ['number']

    def __str__(self):
        return self.number

class Instructor(models.Model):
    instructor_id = models.CharField(max_length=9, primary_key=True)
    name = models.CharField(max_length=40)

    class Meta:
        ordering = ['instructor_id']

    def __str__(self):
        return self.name

class MeetingTime(models.Model):
    meeting_id = models.CharField(max_length=5, primary_key=True)
    meeting_day = models.CharField(max_length=11)
    meeting_start_time = models.TimeField()
    meeting_end_time = models.TimeField()

    class Meta:
        verbose_name = 'Meeting Time'
        db_table = 'meetingtime'

    def __str__(self):
        return self.meeting_id

class Course(models.Model):
    code = models.CharField(max_length=13, primary_key=True)
    name = models.CharField(max_length=40)
    numb_of_students = models.IntegerField()
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    credit = models.DecimalField(max_digits=5,decimal_places=1)

    class Meta:
        ordering = ['code']

    def __str__(self):
        return self.name
