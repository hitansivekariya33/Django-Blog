from django.shortcuts import render,HttpResponseRedirect,redirect 
from .form import Signup
from django.contrib import messages
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import AuthenticationForm 
from django.views.generic import View

# signup 
class Sign_up(View):
    template_name = 'signup.html'
    def post(self,request):
        form = Signup(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return HttpResponseRedirect("signin/")
        return render(request,self.template_name,{'signup_form':form})
    def get(self,request):
        form = Signup()
        return render(request,self.template_name,{'signup_form':form})

#login 
class Sign_in(View):
    template_name = 'login.html'
    def post(self, request):
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect("/blog/")
        return render(request,self.template_name,{'login_form':form})
        
    def get(self,request):
        form = AuthenticationForm()
        return render(request,self.template_name,{"login_form":form})

#logout
def sign_out(request):
    logout(request)
    return HttpResponseRedirect('/accounts/signin/')