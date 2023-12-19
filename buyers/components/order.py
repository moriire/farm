from django_unicorn.components import UnicornView
from users.models import User, Profile
from django.shortcuts import redirect
from farmers.models import SelectedItems
import json
import requests
class OrderView(UnicornView):
    items = SelectedItems.objects.none()
    total_price:float = 0.0
    order_count:int = 0
    db_unit = 1
    authorization_url=''

    def mount(self):
        self.update()

    def update(self):
        self.items = SelectedItems.objects.filter(item__farmer = self.request.user, noted=False)#.select_related('item')#.prefetch_related('buyer')
        #print(self.items)
        self.order_count = len(self.items)
        self.get_total()
        

    def get_total(self):
        price_list = [i.item.price*int(i.unit) for i in self.items]
        self.total_price = sum(price_list)

    def paylink(self, email):
        price_list = [i.item.price*int(i.unit) for i in self.items]
        print(price_list)
        total = str(sum(price_list))
        print(total)
        print(type(total))
        
        req = requests.post("https://api.paystack.co/transaction/initialize",
                        headers={"Authorization": "Bearer sk_test_69c5ade1fdc1eaf0cdf71269f3e9dd8c517b445e",
                                "Content-Type": "application/json"
                                },
                                json={'email': email, 'amount': total}
                        )
        print(req)
        res = req.json()
        print(res)
        self.authorization_url = res.get('data').get('authorization_url')
        
