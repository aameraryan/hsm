from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Setting(models.Model):
    Hospital_Name = models.CharField(max_length=200)
    Background_Image = models.ImageField(blank=True, null=True, upload_to='logos')
    Vision = models.TextField(blank=True, null=True)
    Mission = models.TextField(blank=True, null=True)
    Address = models.TextField(blank=True, null=True)
    Location = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.Hospital_Name


class Floor(models.Model):
    Name = models.CharField(max_length=200)
    Shift_Leader = models.CharField(max_length=200, blank=True, null=True)
    Extra_Details = models.TextField(blank=True, null=True)
    User = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)


    def __str__(self):
        return self.Name

    def get_patient_count(self):
        return self.patient_set.filter(Discharged=False).count()
    get_patient_count.short_description = 'Patients Under Treatment'

    def get_division_count(self):
        return self.division_set.all().count()

    get_division_count.short_description = 'Divisions'


class Division(models.Model):
    Name = models.CharField(max_length=200, blank=True, null=True)
    Floor = models.ForeignKey(Floor, on_delete=models.SET_NULL, null=True, blank=True)
    Doctor1 = models.CharField(max_length=200, blank=True, null=True, verbose_name='Doctor1 on call')
    Doctor2 = models.CharField(max_length=200, blank=True, null=True, verbose_name='Doctor2 on call')
    Display_Name = models.CharField(max_length=200, default='Doctors On Call')

    def __str__(self):
        return self.Name

    def active_patients(self):
        return self.patient_set.filter(Discharged=False)


class Doctor(models.Model):
    Name = models.CharField(max_length=200)
    Extra_Details = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.Name

    def get_patient_count(self):
        return self.patient_set.filter(Discharged=False).count()

    get_patient_count.short_description = 'Patients Under Treatment'



class Nurse(models.Model):
    Name = models.CharField(max_length=200)
    Extra_Details = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.Name

    def get_patient_count(self):
        return self.patient_set.filter(Discharged=False).count()

    get_patient_count.short_description = 'Patients Under Treatment'


class Patient(models.Model):
    Name = models.CharField(max_length=200, blank=True, null=True)
    Room = models.CharField(max_length=200, blank=True, null=True)
    Division = models.ForeignKey(Division, on_delete=models.SET_NULL, blank=True, null=True)
    Floor = models.ForeignKey(Floor, on_delete=models.SET_NULL, blank=True, null=True)
    Doctor_Attending = models.ForeignKey(Doctor, on_delete=models.SET_NULL, blank=True, null=True)
    Nurse_Attending = models.ForeignKey(Nurse, on_delete=models.SET_NULL, blank=True, null=True)
    Discharged = models.BooleanField(default=False)

    def __str__(self):
        return self.Name

