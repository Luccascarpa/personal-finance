from django.contrib.auth.models import User, Group
from django.db.models import query_utils
from django.db.models.query import QuerySet
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, GroupSerializer, EarningSerializer, ExpenseSerializer, InvestmentSerializer
from .models import Earning, Expense, Investment


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class EarningViewSet(viewsets.ModelViewSet):
    """
    API endpoint to read and write earnings
    """
    queryset = Earning.objects.all()
    serializer_class = EarningSerializer
    permission_classes = [permissions.IsAuthenticated]


class ExpenseViewSet(viewsets.ModelViewSet):
    """
    API endpoint to read and write expenses
    """
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]    


class InvestmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint to read and write investment
    """
    queryset = Investment.objects.all()
    serializer_class = InvestmentSerializer
    permission_classes = [permissions.IsAuthenticated]