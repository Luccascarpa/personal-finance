from django.contrib import admin

from .models import Earning, Expense, Investment

admin.site.register(Earning)
admin.site.register(Expense)
admin.site.register(Investment)
