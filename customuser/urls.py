from django.urls import path
from customuser import views

urlpatterns = [
    path('register',views.UserCreate.as_view(),name='register'),
    path('',views.userlogin,name='login'),
    path('logout_view',views.logout_view,name='logout'),

]