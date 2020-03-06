from django.urls import path
from leave import views

urlpatterns = [
        path('leave_apply',views.leaveapply,name='leave'),
        path('leaves',views.leave_list,name='leave_list'),
        path('delete_leaves/<int:pk>',views.delete_list,name='leave_delete'),


]