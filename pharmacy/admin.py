from django.contrib import admin

# Register your models here.
from .models import Medicine,  Customer, Sale, Tickets

admin.site.register(Medicine)
admin.site.register(Customer)
admin.site.register(Sale)
admin.site.register(Tickets)

