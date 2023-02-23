from django.shortcuts import render,HttpResponseRedirect,redirect 
from .form import Signup
from django.contrib import messages
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import AuthenticationForm 

# signup function
def sign_up(request):
    if request.method == "POST":
        form = Signup(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return HttpResponseRedirect("signin/")
    form = Signup()
    return render(request,'signup.html',{'signup_form':form})

#login function
def sign_in(request):
	if request.method == "POST":
		form = AuthenticationForm(request=request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return HttpResponseRedirect("/blog/")
		# 	else:
		# 		messages.error(request,"Invalid username or password.")
		# else:
		# 	messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request,"login.html",{"login_form":form})

#logout function
def sign_out(request):
    logout(request)
    return HttpResponseRedirect('/accounts/signin/')