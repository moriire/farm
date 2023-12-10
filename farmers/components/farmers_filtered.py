from django_unicorn.components import UnicornView
from farmers.models import Items
class FarmersFilteredView(UnicornView):
    items:Items = Items.objects.none()
    produce:str=''
    quantity:str=''
    items_checked = []

    def mount(self):
        tok = self.request.GET
        self.produce = tok.get('produce', '')
        self.quantity = tok.get('quantity', '')
        self.update()
        return super().mount()
    
    def update(self):
        print('refreshing......')
        self.items = Items.objects.select_related('farmer').all().filter(produce__name=self.produce, quantity=self.quantity)

    def checked(self, item):
        self.items_checked.append(item)
        print("checked")