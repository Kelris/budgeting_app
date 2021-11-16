from rest_framework import serializers

from budget.models import Category, Expenses, Income


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ExpensesSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Expenses
        fields = [
            'id',
            'name',
            'value',
            'category',
            'date',
        ]


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = [
            'id',
            'name',
            'value',
            'date',
        ]
