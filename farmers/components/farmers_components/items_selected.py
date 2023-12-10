from django_unicorn.components import UnicornView, LocationUpdate
from typing import List, Dict
from farmers.models import Items
from django.shortcuts import redirect

class ItemsSelectedView(UnicornView):
    carts: List[int] = []
    total_price = 0

    def mount(self):
        self.carts = self.component_kwargs['carts']
        return super().mount()