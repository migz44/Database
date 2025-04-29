from django.db import models

# Create your models here.
class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    names = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    phone = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=150)
    weight = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    gender = models.CharField(max_length=10, default="Male")


    class Meta:
        db_table = 'customers'
# python manage.py makemigrations
# python manage.py migrate
