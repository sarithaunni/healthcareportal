from django.urls import path
from appoinments import views

urlpatterns = [
    path('appoinment',views.AppoinmentCreate.as_view(),name='appoinment_create'),
    path('appoinment_detail/<int:id>',views.appoinment_detail,name='appoinment_detail'),
    path('appoinment_delete/<int:pk>',views.deleteAppoinment,name='appoinment_delete'),
    path('appoinment_update/<int:pk>',views.update_appoinment,name='update_appoinment'),


]