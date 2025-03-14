from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer
from patients.models import Patient
from doctors.models import Doctor

class PatientDoctorMappingListCreateView(generics.ListCreateAPIView):
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        patient_id = self.request.data.get("patient")
        doctor_id = self.request.data.get("doctor")

        # Check if patient exists and belongs to the user
        try:
            patient = Patient.objects.get(id=patient_id, user=self.request.user)
        except Patient.DoesNotExist:
            raise ValidationError("Patient not found or unauthorized")

        # Check if doctor exists
        if not Doctor.objects.filter(id=doctor_id).exists():
            raise ValidationError("Doctor not found")

        # Save mapping
        serializer.save()

class PatientDoctorMappingDetailView(generics.DestroyAPIView):
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated]
