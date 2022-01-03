from datetime import datetime

from django.db import models


class Earning(models.Model):
    category = models.CharField(max_length=200)
    subcategory = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    value = models.FloatField()
    date = models.DateField(default=datetime.today().strftime('%Y-%m-%d'))

    def __str__(self):
        return f'{self.category} - {self.subcategory}: R${self.value}'


class Expense(models.Model):
    category = models.CharField(max_length=200)
    subcategory = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    value = models.FloatField()
    date = models.DateField(default=datetime.today().strftime('%Y-%m-%d'))

    def __str__(self):
        return f'{self.category} - {self.subcategory}: R${self.value}'


class Investment(models.Model):
    category = models.CharField(max_length=200)
    subcategory = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    value = models.FloatField()
    date = models.DateField(default=datetime.today().strftime('%Y-%m-%d'))

    def __str__(self):
        return f'{self.category} - {self.subcategory}: R${self.value}'