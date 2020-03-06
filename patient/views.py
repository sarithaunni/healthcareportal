from django.shortcuts import render,redirect,get_object_or_404
from .models import Patient
from doctor.models import Doctor
from patient.forms import PatientForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from appoinments.models import Appoinment


class PatientCreate(CreateView):
    model=Patient
    fields=['gender','email','ph','birthdate','address','city','pincode','state','country','blood','photo']
    success_url=reverse_lazy('patient')
    def form_valid(self,form):
        self.object=form.save(commit=False)
        self.object.user=self.request.user
        self.object.save()
        return redirect(self.get_success_url())


def patient_home(request):
    return render(request,'patient/patient_home.html',{})

def patientappoinment(request):
    appoinments=Appoinment.objects.all().filter(user=request.user)
    return render(request,'patient/patient_appoinment.html',{"apnt":appoinments})

def patientdetail(request):
    patient=Patient.objects.all().filter(user=request.user).first()
    return render(request,'patient/patient_detail.html',{'object':patient})

def update_patient(request, pk):
    print(pk)
    update_object=get_object_or_404(Patient,pk=pk)
    print(update_object)
    patient_form=PatientForm(instance=update_object)

    if(request.method=='POST'):
        patient_form=PatientForm(request.POST or None, instance=update_object)
        if patient_form.is_valid():
            patient_form.save()
            return redirect('patient_home')

    return render(request, 'patient/patient_form.html', { "form" : patient_form })

def doctor_list(requset):
    print(requset)
    query=requset.GET.get('t')
    qs=Doctor.objects.all()

    if query is not None:
        qs=qs.filter(specilized_in__icontains=query)
    
    return render(requset,'patient/doctor_list_home.html',{'objectlist': qs })
    
    
    #return render(requset,'patient/doctor_list_home.html',{'objectlist': Doctor.objects.all() })