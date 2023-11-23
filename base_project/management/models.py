from django.db import models

# Create your models here.
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

    def __str__(self):
        return f'Student: {self.student_name}'