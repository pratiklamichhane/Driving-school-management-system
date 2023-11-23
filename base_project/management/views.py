from django.shortcuts import render 
from .models import Student
# Create your views here.
def index(request):
    return render(request , 'management/index.html' , {
        'students' : Student.objects.all().order_by('-id'),
        'total_students' : Student.objects.count(),
        'active_students_count' : Student.objects.filter(enrollment_status='ACTIVE').count(),
        'unpaid_invoices' : Student.objects.filter(payment_status='UNPAID').count(),
    })