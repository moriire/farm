from django_unicorn.components import UnicornView, LocationUpdate
from farmers.models import Items, Crop
from users.models import User
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
import uuid

class AddProduceView(UnicornView):
    crops:Crop= Crop.objects.none()
    items:Items = Items.objects.none()
    item:Items = None
    farmer:None
    produce:str = ""
    price:float = 0.0
    quantity:str = 1
    measurememt:str=""
    desc: str = ""
    img=''

    def mount(self):
        self.crops= Crop.objects.all()
        self.items= Items.objects.filter(farmer = self.request.user)
        self.farmer = self.request.user#component_kwargs.get('user')
    
    def update(self):
        self.produce = ""
        self.price = 0.0
        self.quantity = 1
        self.measurememt =""
        self.desc= ""
        #self.parent.update()
        
    def save(self):
        Items.objects.create(
            farmer = self.farmer,
            produce = self.produce,
            price = self.price,
            quantity = self.quantity,
            measurement = self.measurememt,
            desc = self.desc
        )
        self.update()
        print("success")