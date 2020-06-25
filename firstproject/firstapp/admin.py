from django.contrib import admin
from .models import Customer
from .models import FoodItem
from .models import Order
from .models import Menu
from .models import Payment

admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(FoodItem)
admin.site.register(Menu)
admin.site.register(Payment)