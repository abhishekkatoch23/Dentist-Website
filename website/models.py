from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.EmailField()
    message=models.TextField()
    def __str__(self):
        return self.name
class Appointment(models.Model):
    name=models.CharField(max_length=122)
    email=models.EmailField()
    message=models.TextField()
    phone=models.CharField(max_length=10)
    adderss=models.CharField(max_length=200)
    first_choice_appointment=models.CharField(max_length=50)
    date=models.CharField(max_length=80)
    message=models.TextField()
    def __str__(self):
        return self.name