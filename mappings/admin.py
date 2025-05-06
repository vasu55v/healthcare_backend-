from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import PatientDoctorMapping


class PatientDoctorMappingAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'assigned_date', 'user')
    list_filter = ('assigned_date',)
    search_fields = ('patient__first_name', 'patient__last_name', 'doctor__first_name', 'doctor__last_name')
    date_hierarchy = 'assigned_date'


admin.site.register(PatientDoctorMapping, PatientDoctorMappingAdmin)