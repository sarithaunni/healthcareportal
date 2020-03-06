from django.shortcuts import render,redirect,get_object_or_404
from .forms import AppoinmentForm,UpdateAppoinmentForm
from .models import Appoinment
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.http.response import JsonResponse

# Create your views here.

class AppoinmentCreate(CreateView):
    form_class=AppoinmentForm
    model=Appoinment
    template_name='appoinments/apnt_create.html'
    success_url=reverse_lazy('patient_appoinment_home')

    def form_valid(self,form):
        self.object=form.save(commit=False)
        self.object.user=self.request.user
        self.object.save()
        return redirect(self.get_success_url())
def appoinment_detail(request,id):
    appoinment=get_object_or_404(Appoinment,pk=id)
    return render(request,'appoinments/apnt_detail.html',{'object':appoinment})

def deleteAppoinment(request, pk):
    delete_object=get_object_or_404(Appoinment,pk=pk)
    delete_object.delete()

    if request.is_ajax():
        return JsonResponse({
            'message':'Item deleted'
        })


    #return redirect('patient_appoinment_home')

def update_appoinment(request,pk):
    update_object=get_object_or_404(Appoinment,pk=pk)
    print(update_object)
    appoinment_form=UpdateAppoinmentForm(instance=update_object)
    if(request.method=='POST'):
        appoinment_form=UpdateAppoinmentForm(request.POST or None, instance=update_object)
        if appoinment_form.is_valid():
            appoinment_form.save()
            if request.user.type=='Doctor':
                return redirect('dr_appoinment')
            return redirect('patient_appoinment_home')
    return render(request, 'appoinments/apnt_create.html', { "form" : appoinment_form })