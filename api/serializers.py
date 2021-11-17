from rest_framework import serializers

from budget.models import Category, Expenses, Income


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class UserFilteredPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        request = self.context.get('request', None)
        queryset = super(UserFilteredPrimaryKeyRelatedField, self).get_queryset()  # noqa
        if not request or not queryset:
            return None
        return queryset.filter(owner=request.user)


class ExpensesSerializer(serializers.ModelSerializer):
    category = UserFilteredPrimaryKeyRelatedField(
        queryset=Category.objects.all()
    )

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
