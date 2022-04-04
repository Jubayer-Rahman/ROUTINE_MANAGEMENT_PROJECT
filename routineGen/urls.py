from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('addInstructors/', views.addInstructors, name='addInstructors'),
    path('deleteInstructors/<str:pk>', views.deleteInstructors, name='deleteInstructors'),
    path('editInstructors/<str:pk>/', views.editInstructors, name='editInstructors'),
    path('addRooms/', views.addRooms, name='addRooms'),
    path('deleteRooms/<str:pk>', views.deleteRooms, name='deleteRooms'),
    path('editRooms/<str:pk>/', views.editRooms, name='editRooms'),
    path('addCourses/', views.addCourses, name='addCourses'),
    path('deleteCourses/<str:pk>', views.deleteCourses, name='deleteCourses'),
    path('editCourses/<str:pk>/', views.editCourses, name='editCourses'),
    path('routine/', views.routine_view, name='routine'),
]
