from django.http import HttpResponseRedirect
from django.shortcuts import render , get_object_or_404
from django.urls import reverse
from .models import Student , Staffs
from django.db.models import Count

# Create your views here.
def index(request):
    return render(request , 'management/index.html' , {
        'students' : Student.objects.all().order_by('-id'),
        'total_students' : Student.objects.count(),
        'active_students_count' : Student.objects.filter(enrollment_status='ACTIVE').count(),
        'unpaid_invoices' : Student.objects.filter(payment_status='UNPAID').count(),
        'total_staffs' : Staffs.objects.count()
    })

def view_student(request , id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def staffs(request):
    staff_members = Staffs.objects.all()

    for staff in staff_members:
        active_students_count = staff.students_assigned.filter(
            enrollment_status='ACTIVE'
        ).count()

        total_students_count = staff.students_assigned.count()
        staff.active_students_count = active_students_count
        staff.total_students_count = total_students_count

    return render(request, 'management/staffs.html', {
        'staffs': staff_members
    })

def view_staff(request , id):
    student = Staffs.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def students_assigned_to_staff(request, staff_id):
    staff = get_object_or_404(Staffs, pk=staff_id)

    return render(request, 'management/staff_students.html', {
        'staff': staff
    })