from django_unicorn.components import UnicornView, QuerySetType, LocationUpdate
from farmers.models import Items, SelectedItems
from django.shortcuts import redirect


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
    
    def update(self):#produce list on mount
        print('refreshing......')
        self.items = Items.objects.select_related('farmer').all()#.filter(img=False)#produce=produce, quantity=quantity)
        for child in self.children:
            if hasattr(child, 'update_produce'):
                child.update_produce()

    def save_to_db(self):
        for item in self.items_checked:
            item_instance = Items.objects.get(pk = item.get('pk'))
            SelectedItems.objects.create(
                buyer = self.request.user,
                item = item_instance
            )
            self.items_checked.clear()
        #return LocationUpdate(redirect('cart'), 'success')
        return redirect('cart')
    
    def del_item(self, x):
        self.items_checked.remove(x)
        print('deleting')
        #self.checked()


