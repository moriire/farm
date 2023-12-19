from django.db import models
from farmers.models import Items, SelectedItems
from users.models import User

class CartItems(models.Model):
    item = models.ManyToManyField(SelectedItems, related_name="add_item", blank=True)
    buyer =  models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    unit = models.IntegerField(default=1)
    created_on = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.buyer.get_full_name()
    