from django.contrib import admin

# Register your models here.
from .models import Patient


class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'user', 'phone_number', 'created_at')
    list_filter = ('gender', 'created_at')
    search_fields = ('first_name', 'last_name', 'phone_number')
    date_hierarchy = 'created_at'


admin.site.register(Patient, PatientAdmin)

