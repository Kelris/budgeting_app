from rest_framework import generics

from api.serializers import (CategorySerializer, ExpensesSerializer,
                             IncomeSerializer)
from budget.models import Category, Expenses, Income


class CategoriesListAndCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get_queryset(self):
        user = self.request.user
        return Category.objects.filter(owner=user)


class CategoryDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        user = self.request.user
        return Category.objects.filter(owner=user)


class ExpensesListAndCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ExpensesSerializer
    queryset = Expenses.objects.all()

    def get_queryset(self):
        user = self.request.user
        return Expenses.objects.filter(category__owner=user)


class ExpenseDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExpensesSerializer
    queryset = Expenses.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        user = self.request.user
        return Expenses.objects.filter(category__owner=user)


class IncomeListAndCreateAPIView(generics.ListCreateAPIView):
    serializer_class = IncomeSerializer
    queryset = Income.objects.all()

    def get_queryset(self):
        user = self.request.user
        return Income.objects.filter(owner=user)


class IncomeDetailUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = IncomeSerializer
    queryset = Income.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        user = self.request.user
        return Income.objects.filter(owner=user)
