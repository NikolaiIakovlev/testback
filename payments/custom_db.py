"""Скрипт для автозаполнения БД"""
import random
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','payments.settings')

import django
django.setup()

from django.db import models
from django.contrib.auth.models import User
from faker import Faker
from payment_requests.models import Requisites, Payment

fake = Faker()

# Создание 100 реквизитов
for _ in range(100):
    Requisites.objects.create(
        payment_type=random.choice(['card', 'bank_account']),
        account_type=fake.word(),
        owner_name=fake.name(),
        phone_number=fake.phone_number(),
        limit=random.uniform(0, 10000)
    )

# Получение всех реквизитов
requisites = Requisites.objects.all()

# Создание 5000 заявок
for _ in range(5000):
    Payment.objects.create(
        amount=random.uniform(0, 1000),
        requisites=random.choice(requisites),
        status=random.choice(['pending', 'paid', 'canceled'])
    )
