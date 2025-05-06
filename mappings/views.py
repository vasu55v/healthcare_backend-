from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer, PatientDoctorMappingDetailSerializer
from patients.models import Patient


class PatientDoctorMappingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return PatientDoctorMappingDetailSerializer
        return PatientDoctorMappingSerializer
    
    def get_queryset(self):
        return PatientDoctorMapping.objects.filter(user=self.request.user)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response({
            'success': True,
            'message': 'Doctor assigned to patient successfully',
            'data': serializer.data
        }, status=status.HTTP_201_CREATED, headers=headers)
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({
            'success': True,
            'data': serializer.data
        })
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            'success': True,
            'message': 'Doctor removed from patient successfully'
        }, status=status.HTTP_204_NO_CONTENT)
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response({
                'success': True,
                'data': serializer.data
            })
        
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            'success': True,
            'data': serializer.data
        })
    
    @action(detail=False, methods=['get'], url_path='patient/(?P<patient_id>[^/.]+)')
    def get_patient_doctors(self, request, patient_id=None):

        #this method gets all doctors assign to specific doctor 

        try:
            # Verify patient belongs to current user(in which doctor)
            patient = Patient.objects.get(id=patient_id, user=request.user)
            mappings = PatientDoctorMapping.objects.filter(patient=patient)
            serializer = self.get_serializer(mappings, many=True)
            return Response({
                'success': True,
                'data': serializer.data
            })
        except Patient.DoesNotExist:
            return Response({
                'success': False,
                'error': 'Patient not found or you do not have permission to view this patient'
            }, status=status.HTTP_404_NOT_FOUND)