from rest_framework import serializers
from .models import PatientDoctorMapping
from patients.serializers import PatientSerializer
from doctors.serializers import DoctorSerializer


class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDoctorMapping
        fields = ['id', 'patient', 'doctor', 'assigned_date', 'notes']
        read_only_fields = ['id', 'assigned_date']
    
    def create(self, validated_data):
        user = self.context.get('request').user
        mapping = PatientDoctorMapping.objects.create(user=user, **validated_data)
        return mapping
        
    def validate(self, data):
        # Check that if patient belongs to the current user
        patient = data.get('patient')
        if patient.user != self.context['request'].user:
            raise serializers.ValidationError({"patient": "You can only assign doctor to your own patients."})
        return data


class PatientDoctorMappingDetailSerializer(PatientDoctorMappingSerializer):
    patient = PatientSerializer(read_only=True)
    doctor = DoctorSerializer(read_only=True)