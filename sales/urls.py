from django.urls import path

# using class based views
from .views import (home_view,SaleListView,SaleDetailView)     


app_name = "sales"
urlpatterns = [
    path("",home_view,name="home"),     #http://localhost:8000/sales/
    path("sales/",SaleListView.as_view(),name="sales_list"), ##http://localhost:8000/sales/
    path("sales/<pk>",SaleDetailView.as_view(),name="detail"), #http://localhost:8000/sales/sales/2
]
