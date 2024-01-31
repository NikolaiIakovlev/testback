from django.db import models


class Requisites(models.Model):
    # Выбор типа оплаты
    PAYMENT_TYPE_CHOICES = (
        ('card', 'Карта'),
        ('bank_account', 'Платежный счет'),
    )
    payment_type = models.CharField(max_length=20, choices=PAYMENT_TYPE_CHOICES)  # Поле для хранения выбранного типа оплаты
    account_type = models.CharField(max_length=20)  # Тип счета
    owner_name = models.CharField(max_length=100)  # Имя владельца
    phone_number = models.CharField(max_length=20)  # Номер телефона
    limit = models.FloatField()  # Лимит

    def __str__(self):
        return f"{self.owner_name}'s {self.account_type} ({self.payment_type})"


class Payment(models.Model):
    # Статусы оплаты
    STATUS_CHOICES = (
        ('pending', 'Ожидает оплаты'),
        ('paid', 'Оплачена'),
        ('canceled', 'Отменена'),
    )
    amount = models.FloatField()  # Сумма оплаты
    requisites = models.ForeignKey(Requisites, on_delete=models.CASCADE)  # Ссылка на реквизиты для оплаты
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)  # Поле для хранения статуса оплаты

    def __str__(self):
        return f"Payment #{self.id}"
    
