from django.db import models
from farmers.models import Items
from users.models import User
  
class CartItems(models.Model):
    item = models.ForeignKey(Items, on_delete=models.CASCADE, related_name="add_item", null=True)
    buyer =  models.ForeignKey(User, on_delete=models.CASCADE, related_name="user", null=True)
    price = models.FloatField(default=0.0)
    unit = models.IntegerField(default=1)
    def __str__(self) -> str:
        return self.item.produce.name
