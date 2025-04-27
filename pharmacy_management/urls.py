from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import  path
from django.conf import settings
from django.conf.urls.static import static
from pharmacy.views import (
     
    CustomerListView, MedicineListView, create_sale, MedicineCreateView, MedicineUpdateView,
      SaleListView, CustomerCreateView,  CustomerDeleteView, CustomerUpdateView, saleslistdelete, dashboard,
      TicketCreateView, TicketListView, TicketDeleteView, TicketUpdateView, MedicineDeleteView, SaleUpdateView

)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),  # Map the root URL to dashboard_view
   
    path('login/', auth_views.LoginView.as_view(template_name='registeration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
   
    path('customers/', CustomerListView.as_view(), name='customer-list'),
    path('customers/new/', CustomerCreateView.as_view(), name='customer-create'),
    path('customers/<int:pk>/edit/', CustomerUpdateView.as_view(), name='customer-update'),
    path('customers/<int:pk>/delete/', CustomerDeleteView.as_view(), name='customer-delete'),

    path('Medicine/', MedicineListView.as_view(), name='medicine_list'),
    path('Medicine/add/', MedicineCreateView.as_view(), name='medicine_add'),
    path('Medicine/<int:pk>/edit/', MedicineUpdateView.as_view(), name='medicine_edit'),
    path('Medicine/<int:pk>/delete/', MedicineDeleteView.as_view(), name = "medicine_delete"),


    path('create-sale/', create_sale, name='create_sale'),
    path('sales/', SaleListView.as_view(), name='sale_list'),
    path('sales/<int:pk>/delete/', saleslistdelete.as_view(), name='sale_delete'),
    path('sales/<int:pk>/edit/', SaleUpdateView.as_view(), name='sale_edit'),
   
    path('ticket/', TicketListView.as_view(), name='ticket_list'),
    path('ticket_create/', TicketCreateView.as_view(), name = 'ticket_create'),
    path('ticket/<int:pk>/edit/', TicketUpdateView.as_view(), name='ticket_update'),
    path('ticket/<int:pk>/delete/', TicketDeleteView.as_view(), name='ticket_delete'),
    



]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)