from django.urls import path
from . import views  # Import all views

urlpatterns = [
    path('', views.index, name='index'),  # Root URL serves the index.html template
    path('crypto-prices/', views.crypto_prices, name='crypto_prices'),  # API endpoint for chart data
]
