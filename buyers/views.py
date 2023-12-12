from django.views.generic import ListView, DetailView, TemplateView
from .models import Items
from django.contrib.auth.mixins import LoginRequiredMixin
from django_unicorn.components import UnicornView

class IndexView(UnicornView):
    template_name = "index.html"

class Cart(LoginRequiredMixin, TemplateView):
    template_name = "checkout.html"
