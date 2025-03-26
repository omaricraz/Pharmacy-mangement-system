from django import forms
from .models import Medicine, Supplier, PurchaseOrder, Customer, Sale, Expense

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = '__all__'

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'

class PurchaseOrderForm(forms.ModelForm):
    class Meta:
        model = PurchaseOrder
        fields = '__all__'

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['customer', 'medicine', 'quantity']


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'
