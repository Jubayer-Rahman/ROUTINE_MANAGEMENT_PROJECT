from django.contrib import admin
from .models import *

# Register your models here.

'''
admin.site.register(Instructor)
admin.site.register(Room)
admin.site.register(MeetingTime)
admin.site.register(Course)
'''

@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('instructor_id', 'name')

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('number', 'seating_capacity')

@admin.register(MeetingTime)
class MeetingTimeAdmin(admin.ModelAdmin):
    list_display = ('meeting_id', 'meeting_day', 'meeting_start_time', 'meeting_end_time')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'instructor', 'credit', 'numb_of_students')
    list_filter = ('instructor', 'credit')
