from django.shortcuts import render
from django.views.generic import ListView
from .models import Sale

# Create your views here.
def home_view(request):
    context = {}
    return render(request,"sales/sales.html",context)

# class based views
class SaleListView(ListView):
    model = Sale
    template_name = "sales/main.html" #sales/main.html sale=app_name
