from django_unicorn.components import UnicornView
from users.models import User, Profile
from django.shortcuts import redirect
from buyers.models import CartItems
from farmers.models import SelectedItems

class CheckoutFormView(UnicornView):
    total_price = 0
    pay_link:str = ''
    payref = ''
    first_name:str = ''
    last_name:str = ''
    email:str= ''
    phone=''
    state:str=''
    street:str=''
    house_no:str=''
    states:dict[str] = {
                'FC' : 'Abuja',
                'AB' : 'Abia',
                'AD' : 'Adamawa',
                'AK' : 'Akwa Ibom',
                'AN' : 'Anambra',
                'BA' : 'Bauchi',
                'BY' : 'Bayelsa',
                'BE' : 'Benue',
                'BO' : 'Borno',
                'CR' : 'Cross River',
                'DE' : 'Delta',
                'EB' : 'Ebonyi',
                'ED' : 'Edo',
                'EK' : 'Ekiti',
                'EN' : 'Enugu',
                'GO' : 'Gombe',
                'IM' : 'Imo',
                'JI' : 'Jigawa',
                'KD' : 'Kaduna',
                'KN' : 'Kano',
                'KT' : 'Katsina',
                'KE' : 'Kebbi',
                'KO' : 'Kogi',
                'KW' : 'Kwara',
                'LA' : 'Lagos',
                'NA' : 'Nassarawa',
                'NI' : 'Niger',
                'OG' : 'Ogun',
                'ON' : 'Ondo',
                'OS' : 'Osun',
                'OY' : 'Oyo',
                'PL' : 'Plateau',
                'RI' : 'Rivers',
                'SO' : 'Sokoto',
                'TA' : 'Taraba',
                'YO' : 'Yobe',
                'ZA' : 'Zamfara'
    }
    def update(self):
        self.parent.update()
        self.total_price = self.parent.total_price

    def mount(self):
        self.first_name = self.request.user.first_name
        self.last_name = self.request.user.last_name
        self.email = self.request.user.email
        self.phone = self.request.user.phone
        self.state = self.request.user.user_profile.state
        self.street = self.request.user.user_profile.street
        self.house_no = self.request.user.user_profile.house_no
        self.update()
    
    def save(self):
        x = CartItems.objects.create(buyer = self.request.user)
        items = SelectedItems.objects.filter(buyer = self.request.user, noted=False)
        for item in items:
            x.item.add(item)
            item.noted = True
            item.save()
            self.update()
        #self.request.user.first_name = self.first_name
        #self.request.user.last_name = self.last_name
        #elf.request.user.phone = self.email
        #self.request.user.phone = self.phone
        #self.request.user.user_profile.state = self.state
        #self.request.user.user_profile.street = self.street
        #self.request.user.user_profile.house_no = self.house_no
        #self.request.user.save()
        #self.request.user.user_profile.save()
        self.parent.paylink(self.request.user.email)
        print(self.total_price)
        print(self.parent.authorization_url)
        redirect(self.parent.authorization_url)
        

   


