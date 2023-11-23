from django.db import models

# Create your models here.
VECHILE_CHOICES = (
    ("BIKE", "bike"),
    ("SCOOTER", "scooter"),
    ("CAR", "car"),
    ("OTHER", "other"),
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
    final_amount = models.PositiveIntegerField()

    def __str__(self):
        return f'Student: {self.student_name}'