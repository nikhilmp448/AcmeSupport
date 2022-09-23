from department.models import Department
from .forms import CreateDepartment, UserCreationForm
from django.shortcuts import render
from django.contrib import messages , auth
from django.shortcuts import redirect
from user.models import Account
from django.contrib.auth.decorators import login_required
from .decorators import admin_only, allowed_user, unauthenticated_user
from django.contrib.auth.models import Group
# Create your views here.

@unauthenticated_user
def login_user(request):
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


def logout_user(request):
    auth.logout(request)
    return redirect('login')



@login_required(login_url='login')
@admin_only
def home(request):
    return render(request,'home.html')
    pass


@admin_only
def create_user(request):
    form = UserCreationForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            print('valid')
            user=form.save()
            if user.is_admin == True:
                group = Group.objects.get(name='admin')
            else:
                group = Group.objects.get(name='user')
            user.groups.add(group)
            print('data saved successfully')
            return redirect('create_user')
        else:
            print('user is not added')
            messages.info(request,'product not added')
        form = UserCreationForm()
    return render(request,'create_user.html',{'form':form})


@admin_only
def list_users(request):
    users = Account.objects.all()
    context = {'users':users}
    return render(request,'list_user.html',context)


@admin_only
def create_department(request):
    user = request.user
    form = CreateDepartment(request.POST)
    if request.method == "POST":
        if form.is_valid():
            department = form.save(commit=False)
            department.Created_by = user
            department.save()
            return redirect('home')
        else:
            messages.error(request,'field error')
    context={'form':form}
    return render(request,'create_dep.html',context)


@admin_only
def list_dep(request):
    department = Department.objects.all()
    context = {'department':department}
    return render(request,'list_dep.html',context)


@admin_only
def delete_dep(request,id):
    department = Department.objects.filter(id=id)
    if Account.objects.filter(department_id=id).exists():
        messages.error(request,'cant delete')
        return redirect('home')
    else:
        department.delete()
    return redirect('home')
    

@admin_only
def update_dep(request,id):
    department = Department.objects.filter(id=id)
    if request.method == "POST":
        form = CreateDepartment(request.POST,instance=department)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form,'department':department}
    return render(request,'update_dep.html',context)
