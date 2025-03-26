from django.contrib import admin

# Register your models here.
from .models import Medicine, Supplier, PurchaseOrder, Customer, Sale, Expense

admin.site.register(Medicine)
admin.site.register(Supplier)
admin.site.register(PurchaseOrder)
admin.site.register(Customer)
admin.site.register(Sale)
admin.site.register(Expense)