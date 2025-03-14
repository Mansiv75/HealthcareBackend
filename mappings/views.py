from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
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

class PatientDoctorMappingsByPatientView(generics.ListAPIView):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        patient_id = self.kwargs.get("patient_id")
        return PatientDoctorMapping.objects.filter(patient_id=patient_id)

class PatientDoctorMappingDeleteView(generics.DestroyAPIView):
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        mapping_id = kwargs.get("pk")

        try:
            mapping = PatientDoctorMapping.objects.get(id=mapping_id)
        except PatientDoctorMapping.DoesNotExist:
            return Response({"detail": "Mapping not found"}, status=404)

        # Ensure the user owns the patient before allowing deletion
        if mapping.patient.user != request.user:
            raise PermissionDenied("You do not have permission to delete this mapping.")

        mapping.delete()
        return Response({"detail": "Mapping deleted successfully"}, status=204)