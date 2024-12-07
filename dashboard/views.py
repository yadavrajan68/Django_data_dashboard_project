

# Create your views here.
import requests
from django.shortcuts import render
from django.http import JsonResponse

def crypto_prices(request):
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",  # Currency in USD
        "order": "market_cap_desc",
        "per_page": 10,  # Top 10 cryptocurrencies
        "page": 1,
        "sparkline": False
    }

    response = requests.get(url, params=params)
    data = response.json()

    # Process data for Chart.js
    labels = [crypto["name"] for crypto in data]
    prices = [crypto["current_price"] for crypto in data]

    return JsonResponse({"labels": labels, "prices": prices})

def index(request):
    return render(request, 'index.html') 
