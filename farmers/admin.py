from django.contrib import admin
from .models import Items, Crop, SelectedItems
admin.site.register(Crop)
admin.site.register(Items)
admin.site.register(SelectedItems)