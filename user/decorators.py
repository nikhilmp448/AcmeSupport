from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_admin:
            return redirect('home')
        elif request.user.is_authenticated and request.user.is_admin == False:
            return redirect('/')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

def allowed_user(allowed_role=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            print("working>>>>>>>>>")
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_role:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('login')
        return wrapper_func
    return decorator
    
def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group= request.user.groups.all()[0].name
        if group == 'user':
            return redirect('user_homepage')
        if group == 'admin':
            return view_func(request, *args, **kwargs)
        else:
            return redirect('login')
    return wrapper_function