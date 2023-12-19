from django.urls import path, include
#from .views import Farmers, Farmer, Search
from django.views.generic.base import TemplateView
from .views import PostView, PostDetailView
urlpatterns = [
    path('', PostView.as_view(), name="posts"),
    path('<str:pk>/', PostDetailView.as_view(), name="post"),
    #path('search/', Search.as_view(), name='search'),
    #path('<str:pk>/', Farmer.as_view(), name="farmer"),
]