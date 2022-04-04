from django import forms
from .models import *

class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = [
            'instructor_id',
            'name',
        ]
        widgets = {
            'instructor_id' : forms.TextInput(attrs={'class':'form-control'}),
            'name' : forms.TextInput(attrs={'class':'form-control'}),
        }

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = [
            'number',
            'seating_capacity',
        ]
        widgets = {
            'number' : forms.TextInput(attrs={'class':'form-control'}),
            'seating_capacity' : forms. NumberInput(attrs={'class':'form-control'}),
        }

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'code',
            'name',
            'numb_of_students',
            'instructor',
            'credit',
        ]
        widgets = {
            'code' : forms.TextInput(attrs={'class':'form-control'}),
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'numb_of_students' : forms. NumberInput(attrs={'class':'form-control'}),
            'instructor' : forms.Select(attrs={'class':'form-select'}),
            'credit' : forms. NumberInput(attrs={'class':'form-control'}),
        }
