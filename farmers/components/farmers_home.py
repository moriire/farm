from django_unicorn.components import UnicornView, QuerySetType
from farmers.models import Items
from buyers.models import CartItems
class FarmersHomeView(UnicornView):
    items:QuerySetType[Items] = Items.objects.none()#Initialize item from database
    items_checked=[]
    item_count:int = 0
    total_price:float = 0.0
    cart_selected = {'x':0}

    def add_item_value(self, val):#total cart item
        self.total_price += float(val)
    
    def remove_item(self, k):
        print("okay")
        self.item_count = len(self.items_checked)

    def mount(self):
        self.update()
        return super().mount()
    
    def checked(self, item):#for card
        self.items_checked.append(item)
        self.item_count = len(self.items_checked)
        print(self.total_price)
    
    def update(self):#produce list on mount
        print('refreshing......')
        self.items = Items.objects.select_related('farmer', 'produce').all()#.filter(produce=produce, quantity=quantity)
        for child in self.children:
            if hasattr(child, 'update_produce'):
                child.update_produce()

    def save_to_db(self):
        for item in self.items_checked:
            item_instance = Items.objects.get(pk = item.get('pk'))
            CartItems.objects.create(
                item = item_instance,
                buyer = self.request.user
            )


