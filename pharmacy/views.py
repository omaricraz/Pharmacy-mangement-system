from urllib import request
from django.shortcuts import render, redirect
from .models import Customer, Medicine, Sale
from .forms import MedicineForm, CustomerForm, SaleForm 
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy

# ===== Dashboard =====
def dashboard(request):
    medicines = Medicine.objects.all()
    customers = Customer.objects.all()
    context = {'medicines': medicines, 'customers': customers}
    return render(request, 'pharmacy/dashboard.html', context)


class MedicineListView(ListView):
    model = Medicine
    template_name = 'pharmacy/medicine/medicine_list.html'  # Path to the template
    context_object_name = 'medicines'    

# Create Medicine View
class MedicineCreateView(CreateView):
    model = Medicine
    form_class = MedicineForm
    template_name = 'pharmacy/medicine/medicine_create.html'
    success_url = reverse_lazy('inventory_list')

# Edit Medicine View
class MedicineUpdateView(UpdateView):
    model = Medicine
    form_class = MedicineForm
    template_name = 'pharmacy/medicine/medicine_edit.html'
    success_url = reverse_lazy('inventory_list')

def create_sale(request):
    if request.method == 'POST':
        form = SaleForm(request.POST, request.FILES)
        if form.is_valid():
            medicine = form.cleaned_data['medicine']
            quantity = form.cleaned_data['quantity']
            

            # Calculate the total price for the sale
            total_price = medicine.price * quantity

            # Create a Sale record
            sale = form.save(commit=False)
            sale.prices = medicine.price  # Assign price
            sale.total_price = total_price  # Assign total price
            sale.save()

            # Update the medicine quantity after sale
            medicine.quantity -= quantity
            medicine.save()

            return redirect('sale_list')  # Redirect to the sale list view
    else:
        form = SaleForm()

    return render(request, 'pharmacy/sales/sale_create.html', {'form': form})


class SaleListView(ListView):
    model = Sale
    template_name = 'pharmacy/sales/sale_list.html'
    context_object_name = 'sales'
    


# Delete View for sales-list
class saleslistdelete(DeleteView):
    model = Sale
    template_name = 'pharmacy/sales/sale_delete.html'
    success_url = reverse_lazy('sale_list')        
     
  


# CustomerList View (Read)
class CustomerListView(ListView):
    model = Customer
    template_name = 'pharmacy/customers/customer_list.html'
    context_object_name = 'customers'

    

# Create View
class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'pharmacy/customers/customer_form.html'
    success_url = reverse_lazy('customer-list')

# Update View
class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'pharmacy/customers/customer_form.html'
    success_url = reverse_lazy('customer-list')

# Delete View
class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'pharmacy/customers/customer_confirm_delete.html'
    success_url = reverse_lazy('customer-list')    



        