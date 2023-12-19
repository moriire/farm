from django_unicorn.components import UnicornView
from farmers.models import SelectedItems
from django.shortcuts import redirect
import requests

    
class BuyersCartView(UnicornView):
    items = SelectedItems.objects.none()
    total_price = 0

    def update(self):
        self.parent.update()
        self.items = self.parent.items
        self.total_price = self.parent.total_price

    def mount(self):
        self.update()

    def del_item(self, pk):
        SelectedItems.objects.get(id=pk).delete()
        self.update()

    def plus(self, pk):
        this_item = SelectedItems.objects.get(id=pk)
        this_item.unit += 1
        this_item.save()
        self.update()

    def minus(self, pk):
        this_item = SelectedItems.objects.get(id=pk)
        this_item.unit -= 1
        this_item.save()
        self.update()