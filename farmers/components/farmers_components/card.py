from django_unicorn.components import UnicornView

class CardView(UnicornView):
    item: {}
    clicked:bool = False
    def mount(self):
        self.item = self.component_kwargs['item']

    def on_clicked(self):
        self.clicked = True
        print("clicked")

    def add_item(self):
        self.on_clicked()
        self.parent.checked(self.item)
        self.parent.parent.add_item_value(self.item.price)
        print(self.parent.parent.item_count)

    

    



    