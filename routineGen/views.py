from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from .models import *
from .forms import *
import random as rnd
from . import geneticAlgorithm

# Create your views here.

def index(request):
    return render(request, 'routineGen/index.html', context={})

################################################################################

def addInstructors(request):
    form = InstructorForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = InstructorForm()

    instructors = Instructor.objects.all()

    context = {
        'form' : form,
        'instructors' : instructors,
    }
    return render(request, 'routineGen/addInstructors.html', context)

def editInstructors(request, pk):
    if request.method == 'POST':
        instructor = Instructor.objects.get(pk=pk)
        form = InstructorForm(request.POST, instance=instructor)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('addInstructors'))
    else:
        instructor = get_object_or_404(Instructor, pk=pk)
        form = InstructorForm(instance=instructor)
    context = {
        'form' : form,
    }
    return render(request, 'routineGen/editInstructors.html', context)

def deleteInstructors(request, pk):
    if request.method == 'POST':
        instructor = Instructor.objects.get(pk=pk)
        instructor.delete()
        return HttpResponseRedirect(reverse('addInstructors'))

################################################################################

def addRooms(request):
    form = RoomForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = RoomForm()

    rooms = Room.objects.all()

    context = {
        'form' : form,
        'rooms' : rooms,
    }
    return render(request, 'routineGen/addRooms.html', context)

def editRooms(request, pk):
    if request.method == 'POST':
        room = Room.objects.get(pk=pk)
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('addRooms'))
    else:
        room = Room.objects.get(pk=pk)
        form = RoomForm(instance=room)
    context = {
        'form' : form,
    }
    return render(request, 'routineGen/editRooms.html', context)

def deleteRooms(request, pk):
    if request.method == 'POST':
        room = Room.objects.get(pk=pk)
        room.delete()
        return HttpResponseRedirect(reverse('addRooms'))

################################################################################

def addCourses(request):
    form = CourseForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CourseForm()

    courses = Course.objects.all()

    context = {
        'form' : form,
        'courses' : courses,
    }
    return render(request, 'routineGen/addCourses.html', context)

def editCourses(request, pk):
    if request.method == 'POST':
        course = Course.objects.get(pk=pk)
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('addCourses'))
    else:
        course = Course.objects.get(pk=pk)
        form = CourseForm(instance=course)
    context = {
        'form' : form,
    }
    return render(request, 'routineGen/editCourses.html', context)

def deleteCourses(request, pk):
    if request.method == 'POST':
        course = Course.objects.get(pk=pk)
        course.delete()
        return HttpResponseRedirect(reverse('addCourses'))

################################################################################

def routine_view(request):
    routine = geneticAlgorithm()
    context = {
        'routine' : routine,
    }
    return render(request, 'routineGen/routine.html', context)
