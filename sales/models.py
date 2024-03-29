from django.db import models
from products.models import Product
from customers.models import Customer
from profiles.models import Profile
from django.utils import timezone
from .utils import generate_code
from django.shortcuts import reverse

# Create your models here.
class Position(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price= models.FloatField(blank = True)
    created = models.DateTimeField(blank=True)      #adjustable by user


    def save(self,*args,**kwargs):
        self.price = self.product.price * self.quantity
        return super().save(*args,**kwargs)     #extends/ inherit the method from parent django default class


    def __str__(self):
        return f" {self.id} product : {self.product.name} - quantity = {self.quantity}"


class Sale(models.Model):
    transaction_id = models.CharField(max_length=12,blank=True) #auto generated
    positions = models.ManyToManyField(Position)
    total_price = models.FloatField(blank=True,null=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    salesman = models.ForeignKey(Profile,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"sales for the month of {self.created.strftime("%m")} for {self.salesman.user.username}"  

# for making the detail page clickable
    def get_absolute_url(self):
        return reverse("sales:detail", kwargs={"pk": self.pk})
    #detail is the name in the url => path("sales/<pk>",SaleDetailView.as_view(),name="detail")
    

    def save(self,*args,**kwargs):
        if self.transaction_id == "":
            self.transaction_id = generate_code()
        if self.created is None:
            self.created = timezone.now()

        return super().save(*args,**kwargs)

    def get_positions(self):
        return self.positions.all()

class CSV(models.Model):
    file_name = models.FileField(upload_to="csvs")
    activated = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)\


    def __str__(self):
        return str(self.file_name)
