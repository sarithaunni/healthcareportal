from django.shortcuts import render,redirect,HttpResponseRedirect
from .models import Customuser
from .forms import RegistrationForm,LoginForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login,logout
from django import http
from django.contrib import messages



class UserCreate(CreateView):
    form_class=RegistrationForm
    model=Customuser
    template_name='customuser/register.html'
    #fields=['email','username','password','type']
    success_url=reverse_lazy('login')

    def form_valid(self,form):
        self.object=form.save(commit=False)
        self.object.set_password(self.request.POST['password'])
        self.object.save()
        return http.HttpResponseRedirect(self.get_success_url())

def userlogin(request):
    form=LoginForm()
    if(request.method=='POST'):
        form=LoginForm(request.POST)
        print(request.POST)
        if form.is_valid():
            email=form.cleaned_data.get('email')
            password=form.cleaned_data.get('password')
            user=authenticate(request,username=email,password=password)
            if user is not None:
                login(request,user)
                if user.type=='Doctor':
                    return redirect('doctorindex')
                elif user.type=='Patient':
                    return redirect('patient_home')
                else:
                    return redirect('home')
            else:
                messages.add_message(request,messages.ERROR,'invalid username or password!')
                
    return render(request,'customuser/login.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect('login')