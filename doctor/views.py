from django.shortcuts import render,get_object_or_404,redirect
from .models import Doctor
from .forms import DoctorForm
from appoinments.models import Appoinment
from django.utils import timezone


# Create your views here.
def doctorindex(request):
    return render(request,'doctor/doctor_home.html',{})

def doctor_detail(requset):
    doctor=Doctor.objects.all().filter(user=requset.user).first()
    print(doctor)
    return render(requset,'doctor/doctor_detail.html',{'object':doctor})

def doctor_appoinment(request):
    sort=request.GET.get('s')
    print(sort)
    apnt=Appoinment.objects.all().filter(doctor=request.user)
    if sort=='all':
        apnt=Appoinment.objects.all().filter(doctor=request.user)
    elif sort=='today':
        apnt=apnt.filter(appoinmentdate__date=timezone.now())
    elif sort=='not_approved':
        apnt=apnt.filter(status=False)
    else:
        apnt=apnt.filter(status=True)
    return render(request,'doctor/doctor_appoinment.html',{'doctor_appoinment':apnt})


def update_doctor(request, pk):
    print(pk)
    update_object=get_object_or_404(Doctor,pk=pk)
    print(update_object)
    doctor_form=DoctorForm(instance=update_object)

    if(request.method=='POST'):
        doctor_form=DoctorForm(request.POST or None, instance=update_object)
        if doctor_form.is_valid():
            doctor_form.save()
            return redirect('dr_detail')

    return render(request, 'doctor/doctor_form.html', { "form" : doctor_form })

