from django.shortcuts import render
from .models import Payment


def payment_requests(request):
    payment_list = Payment.objects.all()  # Получаем все заявки на оплату из базы данных
    return render(request, 'payment_requests.html',
                  {'payment_list': payment_list})