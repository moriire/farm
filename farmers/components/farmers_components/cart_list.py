from django_unicorn.components import UnicornView, QuerySetType, LocationUpdate

class CartListView(UnicornView):
    cart={}
    x_clicked:bool=False

    def onclick(self):
        self.x_clicked = True
        print(self.x_clicked)

    def mount(self):
        self.cart = self.component_kwargs.get('cart')

    def update(self):
        self.cart = self.component_kwargs.get('cart')

    def del_item(self):
        self.parent.del_item(self.cart)
        #self.onclick()
        #self.parent.items_checked.remove(self.cart)
        #print('deleting')
        #self.update()