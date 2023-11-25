from django.urls import path
from . import views
urlpatterns = [
    path("" , views.index , name="index" ),
    path("<int:id>" , views.view_student , name="view_student" ),
    path("staffs/" , views.staffs , name="staffs" ),
    path("<int:id>" , views.view_staff , name="view_staff" ),
    path('staffs/students/<int:staff_id>/', views.students_assigned_to_staff, name='staff_students'),
    path('addstudent/', views.addStudent , name="addstudent"),
    path('addstaff/', views.addStaff , name="addstaff"),
    path('editstudent/<int:id>/', views.editStudent , name="editstudent"),
    path('editstaff/<int:id>/', views.editStaff , name="editstaff"),
    path('deletestudent/<int:id>', views.deleteStudent , name="deletestudent"),
    path('deletestaff/<int:id>', views.deleteStaff , name="deletestaff")
    ]