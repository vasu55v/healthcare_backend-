from django.db import models

# Create your models here.
from django.conf import settings
from patients.models import Patient
from doctors.models import Doctor


class PatientDoctorMapping(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='mappings')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='doctors')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='patients')
    assigned_date = models.DateField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)
    
    class Meta:
        unique_together = ('patient', 'doctor')
        
    def __str__(self):
        return f"{self.patient} - {self.doctor}"