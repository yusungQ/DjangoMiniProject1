from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Sale


def customer_list(request):
    customer_info = Sale.objects.all()
    context = {
        "customer_key" : customer_info
    }
    return render(request, "sales/index.html", context)

def customer(request, pk):
    
    customer_info = Sale.objects.get(id=pk)
    print(customer_info)
    
    context = {
        "customer_key" : customer_info
    }
    
    return render(request, "sales/age.html", context)