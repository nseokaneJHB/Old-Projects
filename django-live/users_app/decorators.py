from django.http import HttpResponse
from django.shortcuts import redirect


# Decorator function takes in a function as a parameter and allows extra functionality to be added before the
# original function is called

# Stop an authenticated user from viewing the register and login page
def unauthenticated_user(view_func):
    def wrapper_func(request, *arg, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *arg, **kwargs)

    return wrapper_func


# Users for different pages (admin)
# Pass the users
def allowed_users(allowed_roles=[]):
    # Throw in the .view function
    def decorator(view_func):
        def wrapper_func(request, *arg, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *arg, **kwargs)
            else:
                return HttpResponse('You are not authorized to view this page')

        return wrapper_func

    return decorator


# Users for different pages (admin)
def admin_only(view_func):
    def wrapper_func(request, *arg, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'customer':
            return redirect('user-page')

        if group == 'admin':
            return view_func(request, *arg, **kwargs)

    return wrapper_func
