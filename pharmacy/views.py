from django.shortcuts import render, get_object_or_404, redirect
from .models import Medicine, Supplier, PurchaseOrder, Customer, Sale, Expense
from .forms import MedicineForm, SupplierForm, PurchaseOrderForm, CustomerForm, SaleForm, ExpenseForm
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy

# ===== Dashboard =====
def dashboard(request):
    medicines = Medicine.objects.all()
    customers = Customer.objects.all()
    context = {'medicines': medicines, 'customers': customers}
    return render(request, 'pharmacy/dashboard.html', context)



class InventoryListView(ListView):
    model = Medicine
    template_name = 'pharmacy/inventory/inventory_list.html'  # Path to the template
    context_object_name = 'medicines'    

# Create Medicine View
class MedicineCreateView(CreateView):
    model = Medicine
    form_class = MedicineForm
    template_name = 'pharmacy/inventory/create_medicine.html'
    success_url = reverse_lazy('inventory_list')

# Edit Medicine View
class MedicineUpdateView(UpdateView):
    model = Medicine
    form_class = MedicineForm
    template_name = 'pharmacy/inventory/edit_medicine.html'
    success_url = reverse_lazy('inventory_list')

def create_sale(request):
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            medicine = form.cleaned_data['medicine']
            quantity = form.cleaned_data['quantity']
            customer = form.cleaned_data['customer']

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

    return render(request, 'pharmacy/customers/create_sale.html', {'form': form})


class SaleListView(ListView):
    model = Sale
    template_name = 'pharmacy/sale_list.html'
    context_object_name = 'sales'



# List View (Read)
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