from django.http import HttpResponseRedirect
from django.shortcuts import render 
from django.urls import reverse
from .models import Student , Staffs
# Create your views here.
def index(request):
    return render(request , 'management/index.html' , {
        'students' : Student.objects.all().order_by('-id'),
        'total_students' : Student.objects.count(),
        'active_students_count' : Student.objects.filter(enrollment_status='ACTIVE').count(),
        'unpaid_invoices' : Student.objects.filter(payment_status='UNPAID').count(),
    })

def view_student(request , id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))

def staffs(request):
    return render(request , 'management/staffs.html',{
        'staffs' : Staffs.objects.all()
    })

def view_staff(request , id):
    student = Staffs.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))