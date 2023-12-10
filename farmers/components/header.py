from django_unicorn.components import UnicornView

class HeaderView(UnicornView):
    carts:[] = []

    def update(self):
        self.carts = self.component_kwargs.get('carts')