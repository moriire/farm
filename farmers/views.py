from django.views.generic import ListView, DetailView, TemplateView
from .models import Items
from users.models import User
from django.contrib.auth.mixins import LoginRequiredMixin


from django_unicorn.components import UnicornView

class IndexView(UnicornView):
    template_name = "index.html"

class Farmers(LoginRequiredMixin, TemplateView):
    template_name = "farmers.html"

class Search(LoginRequiredMixin, UnicornView):
    template_name = "farmers-search.html"
    
class Farmer(LoginRequiredMixin, DetailView):
    model = Items
    context_object_name = 'farmer'
    template_name = "farmer.html"
    context_object_name = "item"

class CreateItem(LoginRequiredMixin, TemplateView):
    template_name = "post.html"