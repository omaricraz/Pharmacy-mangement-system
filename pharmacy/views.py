from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Customer, Medicine, Sale, Tickets
from .forms import MedicineForm, CustomerForm, SaleForm, TicketForm
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# ===== Dashboard =====
@login_required
def dashboard(request):

    expense_entries = Medicine.objects.all()
    total_expenses = 0
    for expense in expense_entries:
       total_expenses += expense.buyingprice
    expense_context = {"expense" : int(total_expenses)}

    sale_entries = Sale.objects.all()
    sale_context = {"No_of_sales": sale_entries.count()}

    total_revenue = 0
    revenue_entries = Sale.objects.all()
    for revenue in revenue_entries:
        total_revenue += revenue.total_price
       

    
    profit = total_revenue - total_expenses
    profit_context = {"profit": int(profit)}   

    revenue_context = {"total_revenue" : int(total_revenue)}  
    context = {**revenue_context, **sale_context, **expense_context, **profit_context}
      
    return render(request, "front/dashboard.html", context)
   

class MedicineListView(LoginRequiredMixin, ListView):
    model = Medicine
    template_name = 'medicine/medicine_list.html'  # Path to the template
    context_object_name = 'medicines'    

# Delete View
class MedicineDeleteView(LoginRequiredMixin, DeleteView):
    model = Medicine
    template_name = 'medicine/medicine_delete.html'
    success_url = reverse_lazy('medicine_list')    

# Create Medicine View
class MedicineCreateView(LoginRequiredMixin, CreateView):
    model = Medicine
    form_class = MedicineForm
    template_name = 'medicine/medicine_create.html'
    success_url = reverse_lazy('medicine_list')


# Edit Medicine View
class MedicineUpdateView(LoginRequiredMixin, UpdateView):
    model = Medicine
    form_class = MedicineForm
    template_name = 'medicine/medicine_edit.html'
    success_url = reverse_lazy('medicine_list')

@login_required
def create_sale(request):
    if request.method == 'POST':
     
        form = SaleForm(request.POST, request.FILES)
        if form.is_valid():
            medicine = form.cleaned_data['medicine']
            quantity = form.cleaned_data['quantity']
            
        
            # Calculate the total price for the sale
            total_price = medicine.saleprice * quantity

            # Create a Sale record
            sale = form.save(commit=False)
            sale.prices = medicine.saleprice  # Assign price
            sale.total_price = total_price  # Assign total price
            sale.save()

            # Update the medicine quantity after sale
            medicine.quantity -= quantity
            medicine.save()

            return redirect('sale_list')  # Redirect to the sale list view
    else:
        form = SaleForm()

    return render(request, 'sales/sale_create.html', {'form': form}, )


class SaleListView(LoginRequiredMixin, ListView):
    model = Sale
    template_name = 'sales/sale_list.html'
    context_object_name = 'sales'
    

# Delete View for sales-list
class saleslistdelete(LoginRequiredMixin, DeleteView):
    model = Sale
    template_name = 'sales/sale_delete.html'
    success_url = reverse_lazy('sale_list')       

class SaleUpdateView(LoginRequiredMixin, UpdateView):
    model = Sale
    form_class = SaleForm
    template_name = 'sales/sale_edit.html'
    success_url = reverse_lazy('sale_list')
     

# CustomerList View (Read)
class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    template_name = 'customers/customer_list.html'
    context_object_name = 'customers'

    

# Create View
class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customers/customer_form.html'
    success_url = reverse_lazy('customer-list')


# Update View
class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customers/customer_form.html'
    success_url = reverse_lazy('customer-list')


# Delete View
class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    model = Customer
    template_name = 'customers/customer_confirm_delete.html'
    success_url = reverse_lazy('customer-list')    


#Ticket view
class TicketListView(LoginRequiredMixin, ListView):
    model = Tickets
    template_name = 'tickets/ticket_list.html'
    context_object_name = 'tickets'

#Ticket update
class TicketUpdateView(LoginRequiredMixin, UpdateView):
    model = Tickets
    form_class = TicketForm
    template_name = 'tickets/ticket_update.html'
    success_url = reverse_lazy('ticket_list')

#Ticket delete
class TicketDeleteView(LoginRequiredMixin, DeleteView):
    model = Tickets
    template_name = 'tickets/ticket_delete.html'
    success_url = reverse_lazy('ticket_list')    

#Ticket Create
class TicketCreateView(LoginRequiredMixin, CreateView):
    model = Tickets
    form_class = TicketForm
    template_name = 'tickets/ticket_create.html'
    success_url = reverse_lazy("ticket_list")



