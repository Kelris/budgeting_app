from rest_framework import serializers

from budget.models import Category, Expenses, Income


class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Category
        fields = ['id', 'name', 'owner']


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
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Income
        fields = [
            'id',
            'name',
            'value',
            'date',
            'owner',
        ]
