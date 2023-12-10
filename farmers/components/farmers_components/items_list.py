from django_unicorn.components import UnicornView
from farmers.models import Items
class ItemsListView(UnicornView):
    items:Items
    def mount(self):
        self.items = self.parent.items
        return super().mount()
    
    def checked(self, item):
        self.items = self.component_kwargs['items']
        self.parent.items_checked.append(item)
        self.parent.item_count = len(self.parent.items_checked)
        print(self.parent.items_checked)
