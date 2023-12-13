from django_unicorn.components import UnicornView
from users.models import User, Profile
from django.shortcuts import redirect

class CheckoutFormView(UnicornView):
    user: User = None
    profile: Profile = None
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

    def mount(self):
        self.user = User.objects.all().get(pk=self.request.user.id)
        self.profile = Profile.objects.all().get(user=self.request.user.id)
    
    def save(self):#, user:User):
        self.user.save()
        self.profile.save()