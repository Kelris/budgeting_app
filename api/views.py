from rest_framework import generics
from api.serializers import (CategorySerializer, ExpensesSerializer,
                             IncomeSerializer)
from budget.models import Category, Expenses, Income


class CategoriesListAndCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = "id"


class ExpensesListAndCreateAPIView(generics.ListCreateAPIView):
    queryset = Expenses.objects.all()
    serializer_class = ExpensesSerializer


class ExpenseDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExpensesSerializer
    queryset = Expenses.objects.all()
    lookup_field = "id"


class IncomeListAndCreateAPIView(generics.ListCreateAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer


class IncomeDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = IncomeSerializer
    queryset = Income.objects.all()
    lookup_field = "id"
