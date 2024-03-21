from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Sale
from .forms import SalesSearchForm

# Create your views here.
def home_view(request):
    form = SalesSearchForm(request.POST or None)
    context = {
        "form":form
    }
    return render(request,"sales/main.html",context) #serves as home html

# class based views
class SaleListView(ListView):
    model = Sale
    template_name = "sales/main.html" #sales/main.html sale=app_name


class SaleDetailView(DetailView):
    model = Sale
    template_name = "sales/detail.html"

# this is for view based views
#returning sale list
# def sale_list_view(request):
#     sale_list = Sale.objects.all()
#     context = {"sale_list":sale_list}
#     return render(request,"sales/main.html",context)

# #returning the detail page 
# def sale_detail_view(request,pk):
#     sale_detail = Sale.objects.get(pk=pk)
#     context = {"sale_detail":sale_detail}
#     return render(request,"sales/detail.html",context)