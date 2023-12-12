from django_unicorn.components import UnicornView
from users.models import User
from django.shortcuts import redirect

class CheckoutFormView(UnicornView):
    user = User.objects.none()

    def mount(self):
        self.user = User.objects.get(pk=self.request.user.id)
        return super().mount()
    
    def save_user(self):
        self.user.save()