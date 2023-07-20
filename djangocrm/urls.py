from django.contrib import admin
from django.urls import path
from django.urls.conf import include
# from sales.views import Homepage


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Homepage/', include('sales.urls', namespace= "Homepage"))
]
