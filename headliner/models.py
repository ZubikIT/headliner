from django.contrib.auth.models import User
from django.db import models


class HeadlinerTable(models.Model):
    patio_code = models.CharField(max_length=100, unique=True)
    patio_code_group = models.PositiveIntegerField()
    promo_name = models.CharField(max_length=255)
    date_begin = models.DateField(auto_now_add=True)
    date_over = models.DateField()
    price_old = models.CharField(max_length=100)
    price_new = models.CharField(max_length=100)
    promo_type = models.ForeignKey('Promo', on_delete=models.PROTECT, null=True)
    budget = models.CharField(max_length=100)
    budget_type = models.ForeignKey('Budget', on_delete=models.PROTECT, null=True)
    sales_plan = models.CharField(max_length=100)
    utm = models.CharField(max_length=255)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    choice_input = models.BooleanField(default=True)

    def __str__(self):
        return self.promo_name


class Promo(models.Model):
    promo_type_name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.promo_type_name


class Budget(models.Model):
    budget_type_name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.budget_type_name
