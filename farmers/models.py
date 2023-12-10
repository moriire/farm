from django.db import models
from django.contrib.auth.backends import UserModel
User = UserModel()
class Crop(models.Model):
    name = models.CharField(max_length=15)
    def __str__(self) -> str:
        return self.name
    
class Items(models.Model):
    class Quantity(models.TextChoices):
        bag = "BAG"
        farm = "FARM"
        basket = "BASKET"
    farmer =  models.ForeignKey(User, on_delete=models.CASCADE, related_name="farmer_item", null=True)
    produce = models.ForeignKey(Crop, related_name="crop_produce", on_delete=models.CASCADE)
    price = models.FloatField()
    quantity = models.CharField(max_length=20, choices=Quantity.choices, null=True)
    measure = models.CharField(max_length=20, null=True)
    desc = models.TextField(default="")

    def search_url(self):
        return f'/farmers/search/?produce={self.produce}&quantitty={self.quantity}'

    def __str__(self) -> str:
        return self.produce.name
  