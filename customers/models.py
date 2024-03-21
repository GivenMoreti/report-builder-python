from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to="customers",default="default.jpg")

    def __str__(self):
        return self.name