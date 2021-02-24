from contextlib import redirect_stderr

from django.shortcuts import render, redirect
from django.http import HttpResponse

# For inline form
from django.forms import inlineformset_factory

# For registration form
from django.contrib.auth.forms import UserCreationForm

# For login in
from django.contrib.auth import authenticate, login, logout

# To restrict non logged in users from viewing pages
from django.contrib.auth.decorators import login_required

# To add new users to a group
from django.contrib.auth.models import Group

# Import the created decorator
from .decorators import *

from .models import *
from .forms import *

# For errors
from django.contrib import messages


# Create your views here.
@unauthenticated_user
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Account created for ' + username)
            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')

    context = {}
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
    orders = request.user.customer.order_set.all()

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders': orders, 'total_orders': total_orders,
               'delivered': delivered, 'pending': pending}
    return render(request, 'user.html', context)


@login_required(login_url='login')
def accountSettings(request):
    profile = request.user.customer.profile_pic.url
    customer = request.user.customer
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()

    context = {'profile_picture': profile, 'form': form}
    return render(request, 'account_settings.html', context)


@login_required(login_url='login')
@admin_only
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders': orders, 'customers': customers,
               'total_customers': total_customers, 'total_orders': total_orders,
               'delivered': delivered, 'pending': pending}
    return render(request, 'dashboard.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def products(request):
    products = Product.objects.all()

    context = {'products': products}
    return render(request, 'products.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customer(request,  pk):
    customer = Customer.objects.get(id=pk)

    orders = customer.order_set.all()
    total_orders = orders.count()

    context = {'customer': customer, 'orders': orders,
               'total_orders': total_orders}
    return render(request, 'customer.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
# Create model forms from forms.py
def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=6)
    customer = Customer.objects.get(id=pk)

    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    # form = OrderForm(initial={'customer': customer})
    if request.method == 'POST':
        # form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'formset': formset, 'customer': customer}
    return render(request, 'order_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form, 'order': order}
    return render(request, 'update_order.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    # form = OrderForm(instance=order)
    if request.method == 'POST':
        order.delete()
        return redirect('/')

    context = {'order': order}
    return render(request, 'delete.html', context)
