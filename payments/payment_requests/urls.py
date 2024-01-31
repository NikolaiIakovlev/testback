from django.urls import path
from .views import payment_requests
 

urlpatterns = [
    path('', payment_requests, name='payment_requests')
]