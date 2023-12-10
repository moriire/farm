from django_unicorn.components import UnicornView
from farmers.models import Items,Crop
from users.models import User
from django.contrib import messages
import uuid
class CreateItemView(UnicornView):
    farmer:None
    produce:str = ""
    price:float = 0.0
    quantity:str = ''
    measure:str=""
    desc: str = ""
    def mount(self):
        self.farmer = self.request.user
    
    def update(self):
        self.produce = ""
        self.price = 0.0
        self.quantity = ''
        self.measure =""
        self.desc= ""

    def save(self):
        Items.objects.create(
        farmer = self.farmer,
        produce = self.produce,
        price = self.price,
        quantity = self.quantity,
        measure = self.measure,
        desc = self.desc
        )
        self.update()
        messages.success(self.request, "Success")



