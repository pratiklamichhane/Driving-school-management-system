from django import forms 
from .models import Student , Staffs


class StudentForm(forms.ModelForm):
    class Meta :
        model = Student
        fields = ['student_name' ,'phone_number' ,'date_enrolled' ,'time_slot' ,'vehicle_type' ,'enrollment_status' ,'payment_status' , 'final_amount' ,'staff_assigned']
        labels = {
            'student_name' : 'Student Name',
            'phone_number' : 'Phone Number',
            'date_enrolled' : 'Date Enrolled',
            'time_slot' : 'Time Slot',
            'vehicle_type' : 'Vehicle Type',
            'enrollment_status' : 'Enrollment Status' ,
            'payment_status' : 'Payment Status',
            'final_amount' : 'Finalized Amount',
            'staff_assigned' : 'Staff Assigned'
        }
        widgets = {
        'student_name': forms.TextInput(attrs={'class': 'form-control'}),
        'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
        'date_enrolled': forms.DateInput(attrs={'class': 'form-control' , 'type': 'date'}),
        'time_slot': forms.TimeInput(attrs={'class': 'form-control' ,'type': 'time'}), 
        'vehicle_type': forms.Select(attrs={'class': 'form-control'}),
        'enrollment_status': forms.Select(attrs={'class': 'form-control' ,'type': 'dropdown'}), 
        'payment_status': forms.Select(attrs={'class': 'form-control'}),
        'final_amount': forms.NumberInput(attrs={'class': 'form-control'}),
        'staff_assigned': forms.Select(attrs={'class': 'form-control'}),
}
class StaffForm(forms.ModelForm):
    class Meta :
        model = Staffs
        fields = ['staff_name' ,'phone_number' ,'tutor_type']
        labels = {
            'staff_name' : 'Staff Name',
            'phone_number' : 'Phone Number',
            'tutor_type' : 'Tutor Type',
        }
        widgets = {
        'staff_name': forms.TextInput(attrs={'class': 'form-control'}),
        'phone_number': forms.NumberInput(attrs={'class': 'form-control'}),
        'tutor_type': forms.Select(attrs={'class': 'form-control'}),
}

