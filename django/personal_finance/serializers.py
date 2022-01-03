from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Earning, Expense, Investment

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class EarningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Earning
        fields = ['category',
                'subcategory',
                'description',
                'value',
                'date']


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['category',
                'subcategory',
                'description',
                'value',
                'date']


class InvestmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investment
        fields = ['category',
                'subcategory',
                'description',
                'value',
                'date']