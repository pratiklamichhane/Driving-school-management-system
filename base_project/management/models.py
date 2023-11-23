from django.db import models
from django.db.models import Count

# Create your models here.
TUTOR_TYPE = (
    ("BIKE/SCOOTER", "bike/scooter"),
    ("CAR", "car"),
    ("ALL", "all"),
    ("OTHER", "other"),
)
class Staffs(models.Model):
    staff_id = models.AutoField (primary_key=True)
    staff_name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    tutor_type = models.CharField(max_length=50,
                  choices= TUTOR_TYPE,
                  default="BIKE/SCOOTER")
    def get_active_students_count(self):
        return self.students_assigned.filter(
            enrollment_status='ACTIVE'
        ).count()

    def get_total_students_count(self):
        return self.students_assigned.count()

    def __str__(self):
        return  f'{self.staff_name}'
    
    
VECHILE_CHOICES = (
    ("BIKE", "bike"),
    ("SCOOTER", "scooter"),
    ("CAR", "car"),
    ("OTHER", "other"),
)
ENROLLMENT_STATUS = (
    ("ACTIVE", "active"),
    ("HOLD", "hold"),
    ("FINISHED", "finished"),
)
PAYMENT_STATUS = (
    ("PAID", "paid"),
    ("PARTIALLY PAID", "partially paid"),
    ("UNPAID", "unpaid"),
)
class Student(models.Model):
    id = models.AutoField (primary_key=True)
    student_name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    date_enrolled = models.DateField()
    time_slot= models.TimeField()
    vehicle_type = models.CharField(max_length=9,
                  choices= VECHILE_CHOICES,
                  default="BIKE")
    enrollment_status = models.CharField(max_length=9,
                  choices= ENROLLMENT_STATUS,
                  default="ACTIVE")
    payment_status = models.CharField(max_length=30,
                  choices= PAYMENT_STATUS,
                  default="UNPAID")
    final_amount = models.PositiveIntegerField()

    staff_assigned = models.ForeignKey(
        Staffs,
        on_delete=models.SET_NULL,
        blank = True,
        null = True,
        related_name='students_assigned'
    )

    def __str__(self):
        return f'{self.student_name}'
    
