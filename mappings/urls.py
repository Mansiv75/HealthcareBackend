from django.urls import path
from .views import PatientDoctorMappingListCreateView, PatientDoctorMappingDetailView

urlpatterns = [
    path("", PatientDoctorMappingListCreateView.as_view(), name="mapping-list-create"),
    path("<int:pk>/", PatientDoctorMappingDetailView.as_view(), name="mapping-detail"),
]
