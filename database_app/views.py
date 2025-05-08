from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.forms import forms
from django.shortcuts import render, redirect

from database_app.models import Customer
from database_app.my_forms import CustomerForm, LoginForm


# Create your views here.
@login_required
def home(request):
    if request.method == "POST":

        names = request.POST.get('names')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        weight = request.POST.get('weight')
        height = request.POST.get('height')
        gender = request.POST.get('gender')
        print(names, email, phone, password)
        Customer.objects.create(names=names, email=email, phone=phone, password=password, weight=weight, height=height, gender=gender)
        count = Customer.objects.all().count()
        print(f"{count} Customers created successfully")
    return render(request, 'home.html')

@login_required
def show(request):
    data = Customer.objects.all().order_by('-id')
    return render(request, 'show.html',{'data': data})

@login_required
def delete(request, user_id):
    user = Customer.objects.get(id=user_id)
    user.delete()
    return redirect('show-page')

@login_required
def details(request, user_id):
    user = Customer.objects.get(id=user_id)
    return render(request, 'details.html',{'user': user})

@login_required
def add(request):
    if request.method == "POST":
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show-page')
    else:
        form = CustomerForm()
    return render(request,'forms.html',{'form': form})


def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('show-page')

    else:
        form = LoginForm()
    return render(request, 'signin.html', {'form': form})