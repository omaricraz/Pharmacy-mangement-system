from django import forms
from .models import Medicine, Customer, Sale




class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = '__all__'

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['Customer', 'medicine', 'quantity','prescription']



