from django.shortcuts import render,redirect,get_object_or_404
from .models import DoctorLeave
from .forms import LeaveForm
# Create your views here.

def leaveapply(request):
    leave_form=LeaveForm()
    if(request.method=='POST'):
        leave_form=LeaveForm(request.POST)
        if leave_form.is_valid():
            leave_form.save()
            return redirect('leave_list')
    return render(request,'leave/leave_form.html',{'form':leave_form})

def leave_list(request):
    leaves=DoctorLeave.objects.all()
    return render(request,'leave/leave_list.html',{'leave':leaves})

def delete_list(request, pk):
    delete_object=get_object_or_404(DoctorLeave,pk=pk)
    delete_object.delete()
    return redirect('leave_list')