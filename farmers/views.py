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

class UploadFileForm(forms.ModelForm):
    img = forms.ImageField(label="Upload Image", required=False)
    class Meta:
        model = Items
        #exclude =('img',)# ('item', 'farmer', 'produce', 'price', 'bought', 'quantity', 'measurement', 'desc')
        fields = ('img',)#"__all__"

class Upload(LoginRequiredMixin, TemplateView):
    def get(self, request, pk):
        item = Items.objects.get(id=pk)
        if item.DoesNotExist():
            form = UploadFileForm()
        else:
            form = UploadFileForm(instance=item)
        return render(request, "upload.html", {"form": form})

    def post(self, request, pk):
        item = Items.objects.get(pk=pk)
        form = UploadFileForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            #form.save()#
            p = form.save(commit=False)
            print(form)
            p.img = request.FILES.get('img')#cleaned_data.get('img')
            p.save()
            return HttpResponseRedirect("/farmers/add/")
        return render(request, "upload.html", {"form": form})