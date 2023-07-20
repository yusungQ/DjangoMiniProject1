from django.urls import path
from sales.views import customer_list, customer

app_name = "Homepage"

urlpatterns = [
    path('', customer_list),
    path('<pk>/', customer)
]
