from django_unicorn.components import UnicornView, LocationUpdate
from farmers.models import Items, Crop
from users.models import User
from django.contrib import messages
import uuid
class FormCreateView(UnicornView):
    crops:Crop= Crop.objects.none()
    farmer:None
    produce:str = ""
    price:float = 0.0
    quantity:str = ''
    measure:str=""
    desc: str = ""
    def mount(self):
        self.crops= Crop.objects.all()
        self.farmer = self.request.user#component_kwargs.get('user')
    
    def update(self):
        self.produce = ""
        self.price = 0.0
        self.quantity = ''
        self.measure =""
        self.desc= ""
        self.parent.update()


    def save(self):
        Items.objects.create(
        farmer = self.farmer,
        produce = self.produce,
        price = self.price,
        quantity = self.quantity,
        measure = self.measure,
        desc = self.desc
        )
        self.parent.update()
        print("success")