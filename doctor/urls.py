from django.urls import path
from doctor import views

urlpatterns = [
    path('doctorindex',views.doctorindex,name='doctorindex'),
    path('doctor_details',views.doctor_detail,name='dr_detail'),
    path('doctor_appoinments',views.doctor_appoinment,name='dr_appoinment'),
    path('doctor_update/<int:pk>',views.update_doctor,name='dr_update'),



]