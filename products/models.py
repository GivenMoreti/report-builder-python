from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to="products",default="default.jpg")
    price = models.FloatField(help_text="in Rands R")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f" {self.name}  created on {self.created.strftime('%d/%m/%y')}"
    
