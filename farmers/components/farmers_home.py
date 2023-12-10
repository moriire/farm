from django_unicorn.components import UnicornView
from farmers.models import Items
class FarmersHomeView(UnicornView):
    items:Items = Items.objects.none()
    items_checked=[]
    item_count:int = 0
    total_price:float = 0.0
    cart_selected = {'x':0}

    def add_item_value(self, val):
        self.total_price += float(val) 

    def mount(self):
        self.update()
        return super().mount()
    
    def checked(self, item):
        self.items_checked.append(item)
        self.item_count = len(self.items_checked)
        print(self.total_price)
    
    def update(self):
        print('refreshing......')
        self.items = Items.objects.select_related('farmer', 'produce').all()#.filter(produce=produce, quantity=quantity)

    def remove_item(self, k):
        self.items_checked.remove(k)
        self.item_count = len(self.items_checked)
