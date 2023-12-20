from django.urls import path, include
from .views import Farmers, Farmer, Search, CreateProduce
#from .components.farmers_home import FarmersHomeView
urlpatterns = [
    path('', Farmers.as_view(), name="farmers"),
    path('search/', Search.as_view(), name='search'),
    #path('<str:pk>/', Farmer.as_view(), name="farmer"),
    path('add/', CreateProduce.as_view(), name="create-produce"),
]