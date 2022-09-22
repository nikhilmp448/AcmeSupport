from logging import raiseExceptions
from django.shortcuts import render
from django.contrib import messages , auth
from django.shortcuts import redirect
from user.models import Account
from django.contrib.auth.decorators import login_required
# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        field = request.POST.get('field')
        password = request.POST.get('password')
        user = auth.authenticate(email=field,password=password)
        if not user:
            try:
                user = auth.authenticate(email = Account.objects.get(Phone_Number = field) ,password=password)
                print(user)
            except:
                messages.error(request,"credential wrong")
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.error(request,"credential wrong")
    return render(request,'login.html') 

@login_required(login_url='login')
def home(request):
    return render(request,'home.html')
    pass
