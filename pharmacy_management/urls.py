from django.contrib import admin
from django.urls import include, path
from pharmacy.views import dashboard  # Import the dashboard_view function
from pharmacy.views import (
     
    CustomerListView, InventoryListView, create_sale, MedicineCreateView, MedicineUpdateView,
      SaleListView, CustomerCreateView,  CustomerDeleteView, CustomerUpdateView
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),  # Map the root URL to dashboard_view
   

   
    path('customers/', CustomerListView.as_view(), name='customer-list'),
    path('customers/new/', CustomerCreateView.as_view(), name='customer-create'),
    path('customers/<int:pk>/edit/', CustomerUpdateView.as_view(), name='customer-update'),
    path('customers/<int:pk>/delete/', CustomerDeleteView.as_view(), name='customer-delete'),

    path('inventory/', InventoryListView.as_view(), name='inventory_list'),
    path('create-sale/', create_sale, name='create_sale'),


    path('inventory/add/', MedicineCreateView.as_view(), name='medicine_add'),
    path('inventory/<int:pk>/edit/', MedicineUpdateView.as_view(), name='medicine_edit'),


    path('sales/', SaleListView.as_view(), name='sale_list'),




   
]