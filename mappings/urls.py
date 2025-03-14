from django.urls import path
from .views import PatientDoctorMappingListCreateView, PatientDoctorMappingDeleteView, PatientDoctorMappingsByPatientView

urlpatterns = [
    path("", PatientDoctorMappingListCreateView.as_view(), name="mapping-list-create"),
    path("<int:patient_id>/", PatientDoctorMappingsByPatientView.as_view(), name="mapping-by-patient"),
    path("delete/<int:pk>/", PatientDoctorMappingDeleteView.as_view(), name="mapping-delete"),
]
