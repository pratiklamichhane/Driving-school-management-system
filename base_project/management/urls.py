from django.urls import path
from . import views
urlpatterns = [
    path("" , views.index , name="index" ),
    path("<int:id>" , views.view_student , name="view_student" ),
    path("staffs/" , views.staffs , name="staffs" ),
    path("<int:id>" , views.view_staff , name="view_staff" ),
    path('staffs/students/<int:staff_id>/', views.students_assigned_to_staff, name='staff_students'),
    path('addstudent/', views.addStudent , name="addstudent"),
    ]