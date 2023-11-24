from django.http import HttpResponseRedirect
from django.shortcuts import render , get_object_or_404
from django.urls import reverse
from .models import Student , Staffs
from .forms import StudentForm , StaffForm
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

def addStudent(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_student_name = form.cleaned_data['student_name']
            new_phone_number = form.cleaned_data['phone_number']
            new_date_enrolled = form.cleaned_data['date_enrolled']
            new_time_slot = form.cleaned_data['time_slot']
            new_vehicle_type = form.cleaned_data['vehicle_type']
            new_enrollment_status = form.cleaned_data['enrollment_status']
            new_final_amount = form.cleaned_data['final_amount']
            new_staff_assigned = form.cleaned_data['staff_assigned']

            new_student = Student(
                student_name=new_student_name,
                phone_number=new_phone_number,
                date_enrolled=new_date_enrolled,
                time_slot=new_time_slot,
                vehicle_type=new_vehicle_type,
                enrollment_status=new_enrollment_status,
                final_amount=new_final_amount,
                staff_assigned=new_staff_assigned,
            )

            new_student.save()
            return render(request, 'management/addstudent.html', {
                'form': StudentForm(),
                'success': True,
            })
    else:
        form = StudentForm()
    return render(request, 'management/addstudent.html', {
        'form': StudentForm()
    })


def addStaff(request):
    if request.method == 'POST':
        form = StaffForm(request.POST)
        if form.is_valid():
            new_staff_name = form.cleaned_data['staff_name']
            new_phone_number = form.cleaned_data['phone_number']
            new_tutor_type = form.cleaned_data['tutor_type']

            new_staff = Staffs(
                staff_name=new_staff_name,
                phone_number=new_phone_number,
                tutor_type=new_tutor_type,
            )

            new_staff.save()
            return render(request, 'management/addstaff.html', {
                'form': StaffForm(),
                'success': True,
            })
    else:
        form = StaffForm()
    return render(request, 'management/addstaff.html', {
        'form': StaffForm()
    })
