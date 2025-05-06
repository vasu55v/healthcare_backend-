from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Doctor


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'specialization', 'license_number', 'user')
    list_filter = ('specialization', 'years_of_experience')
    search_fields = ('first_name', 'last_name', 'license_number', 'specialization')


admin.site.register(Doctor, DoctorAdmin)
