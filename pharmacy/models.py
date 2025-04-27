from django.db import models

from django.contrib.auth.models import User


# Medicine Model
class Medicine(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    supplier = models.CharField(max_length=255)
    batch_number = models.CharField(max_length=50, unique=True)
    quantity = models.IntegerField()
    saleprice = models.DecimalField(max_digits=10, decimal_places=2)
    buyingprice = models.DecimalField(max_digits=10, decimal_places=2)
    expiry_date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.supplier}"


# Customer Model
class Customer(models.Model):
    name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    prescription = models.ImageField(upload_to='prescriptions/', null=True, blank=True)

    def __str__(self):
        return self.name


# Sale Model
class Sale(models.Model):
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default= "Choose Patient")
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, default="Choose Medicine")
    quantity = models.IntegerField()
    prices = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)  # Add this field
    sale_date = models.DateTimeField(auto_now_add=True)
    prescription = models.ImageField(upload_to='pharmacy/static/prescription_images', null=True, blank=True)

    def __str__(self):
        return f"{self.customer.name} - {self.medicine.name}"
      


class Tickets(models.Model):
    DAY_TIME_CHOICES = [
    ('Morning', 'Morning'),
    ('Afternoon', 'Afternoon'),
    ('Evening', 'Evening'),
]        
    
    AVAILABLE_DOCTORS = [
    ('Jamac', 'Jamac'),
    ('Ismail', 'Ismail'),
    ('Khalid', 'Khalid'),
]    
    name = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="tickets_name", blank=True, null=True) 
    day_time = models.CharField(max_length=100, choices=DAY_TIME_CHOICES, default='Morning')
    doctor = models.CharField(max_length=100, choices=AVAILABLE_DOCTORS, default='Ismail')

    def __str__(self):
        return f"Ticket {self.id} - {self.name}"