from django_unicorn.components import UnicornView
from farmers.models import Items
class FilteredListView(UnicornView):
    items:Items

    def mount(self):
        self.items = self.component_kwargs['items']
        return super().mount()
    
    def update(self):
        print('refreshing......')
        self.items = Items.objects.all()
