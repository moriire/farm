from django_unicorn.components import UnicornView, LocationUpdate
from farmers.models import Items, Crop
from users.models import User
from django.contrib import messages

from django.core.files.storage import FileSystemStorage
import uuid
class FormCreateView(UnicornView):
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
        self.items= Items.objects.all()
        self.farmer = self.request.user#component_kwargs.get('user')
    
    def update(self):
        self.produce = ""
        self.price = 0.0
        self.quantity = 1
        self.measurememt =""
        self.desc= ""
        self.parent.update()
        
    def save(self):
        if self.request.method == 'POST' and self.request.FILES['img']:
            img = self.request.FILES['img']
            fs = FileSystemStorage()
            filename = fs.save(img.name, img)
            filename = fs.url(filename)
        item = Items(
            farmer = self.farmer,
        produce = self.produce,
        price = self.price,
        quantity = self.quantity,
        measurement = self.measurememt,
        desc = self.desc,
        img = filename
        )
        item.save()
        self.parent.update()
        print("success")