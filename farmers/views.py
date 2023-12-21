from django.views.generic import ListView, DetailView, TemplateView
from .models import Items
from users.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django_unicorn.components import UnicornView
from django.http import HttpResponseRedirect
from django.shortcuts import render
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

class CreateProduce(LoginRequiredMixin, TemplateView):
    template_name = "create-produce.html"

class UploadFileForm(forms.Form):
    img = forms.ImageField(label="Upload Image")

class Upload(LoginRequiredMixin, TemplateView):
    def get(self, request, pk=None):
        form = UploadFileForm()
        return render(request, "upload.html", {"form": form})

    def post(self, request, pk):
        item = Items.objects.get(id=pk)
        form = UploadFileForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            #handle_uploaded_file(request.FILES["file"])
            item.save()
            return HttpResponseRedirect("/success/url/")