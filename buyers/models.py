from django.db import models
from farmers.models import Items
from users.models import User

class CartItems(models.Model):
    item = models.ManyToManyField(Items, related_name="add_item")
    buyer =  models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    unit = models.IntegerField(default=1)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self) -> str:
        return self.item.produce.name
    
    def cart_item_amount(self):
        return self.item.price * self.unit
