from django.urls import path, include
from .views import Cart
#from .components.farmers_home import FarmersHomeView
urlpatterns = [
    path('', Cart.as_view(), name="cart"),
    
]