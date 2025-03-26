from django.urls import path
from . import views  # Import views from the same app

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard view
    # Add other app-specific URLs here
]
