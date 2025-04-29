from django.shortcuts import render

from database_app.models import Customer


# Create your views here.
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