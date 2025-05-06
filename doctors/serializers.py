from rest_framework import serializers
from .models import Doctor


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = [
            'id', 'first_name', 'last_name', 'specialization', 
            'license_number', 'phone_number', 'email', 'address',
            'years_of_experience', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def create(self, validated_data):
        user = self.context.get('request').user
        doctor = Doctor.objects.create(user=user, **validated_data)
        return doctor