from collections.abc import Iterable
from django.db import models
from django.utils.safestring import mark_safe
from PIL import Image
from django.contrib.auth.backends import UserModel
User = UserModel()

class Crop(models.Model):
    name = models.CharField(max_length=15)
    def __str__(self) -> str:
        return self.name
    
class Items(models.Model):
    class Measure(models.TextChoices):
        bag = "BAG"
        farm = "FARM"
        basket = "BASKET"
    farmer =  models.ForeignKey(User, on_delete=models.CASCADE, related_name="farmer_item", null=True)
    produce = models.CharField(max_length=30)#ForeignKey(Crop, related_name="crop_produce", on_delete=models.CASCADE)
    price = models.FloatField()
    bought = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)
    measurement = models.CharField(max_length=20, choices=Measure.choices)
    desc = models.TextField(default="")
    img = models.ImageField(blank=True, null=True, upload_to='images/')

    def item_img(self):
        return self.img.url if self.img else ''
    
    def image_tag(self):
        return
    
    def __str__(self) -> str:
        return self.produce
    
    def save(self):
        img = Image.open(self.img.path)
        if img.height>300 or img.height>300:
            new_size = (300, 300)
            img.thumbnail(new_size)
            img.save()
        return super().save()
    
class SelectedItems(models.Model):
    item = models.ForeignKey(Items, related_name="selected_item", on_delete=models.CASCADE)
    buyer =  models.ForeignKey(User, on_delete=models.CASCADE, related_name="selected_item_buyer")
    unit = models.IntegerField(default=1)
    noted = models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.item.produce
    
    def cart_item_amount(self):
        return self.item.price * self.unit

  