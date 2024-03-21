from django.urls import path

# using class based views
from .views import (home_view,SaleListView)     


app_name = "sales"
urlpatterns = [
    path("",home_view,name="home"),
    path("list/",SaleListView.as_view(),name="list")
]