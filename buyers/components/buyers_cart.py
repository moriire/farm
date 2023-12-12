from django_unicorn.components import UnicornView
from buyers.models import CartItems
from django.shortcuts import redirect

class BuyersCartView(UnicornView):
    items = CartItems.objects.none()
    total_price = 0
    order_count:int = 0
    db_unit = 1

    def mount(self):
        self.updateItems()
        print(self.total_price)
        return super().mount()

    def updateItems(self):
        self.items = CartItems.objects.filter(item__farmer = self.request.user).select_related('item', 'buyer')
        self.order_count = len(self.items)
        self.get_total()
        
    def get_total(self):
        price_list = [float(i.item.price)*int(i.unit) for i in self.items]
        self.total_price = sum(price_list)

    def del_item(self, pk):
        print(k)
        CartItems.objects.get(id=pk).delete()
        self.updateItems()

    def plus(self, pk):
        this_item = CartItems.objects.get(id=pk)
        this_item.unit += 1
        this_item.save()
        self.updateItems()

    def minus(self, pk):
        this_item = CartItems.objects.get(id=pk)
        this_item.unit -= 1
        this_item.save()
        self.updateItems()
        

