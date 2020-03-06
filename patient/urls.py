from django.urls import path
from patient import views

urlpatterns = [
    #path('patientcreate',views.PatientCreate.as_view(),name='patientcreate'),
    path('patient_detail',views.patientdetail,name='patient_detail_home'),
    path('patient',views.patient_home,name='patient_home'),
    path('appoinment',views.patientappoinment,name='patient_appoinment_home'),
    path('patient_update/<int:pk>',views.update_patient,name='patient_update'),
    path('patient_doctor_list',views.doctor_list,name='doctor_list'),




]