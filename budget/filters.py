import django_filters
from django.forms import DateInput, TextInput
from django_filters import CharFilter, DateFilter, NumberFilter

from .models import Category, Expenses, Income


class CategoriesFilter(django_filters.FilterSet):
    name = CharFilter(
        field_name='category__name',
        lookup_expr='icontains',
        widget=TextInput(
            {
                'class': 'form-control',
                'placeholder': 'Name contains ...'
            }
        )
    )

    class Meta:
        model = Category
        fields = '__all__'


class ExpensesFilter(django_filters.FilterSet):
    category = CharFilter(
        field_name='category__name',
        lookup_expr='icontains',
        widget=TextInput(
            {
                'class': 'form-control',
                'placeholder': 'Category contains ...'
            }
        )
    )
    start_value = NumberFilter(
        field_name='value',
        lookup_expr='gte',
        widget=DateInput(
            {
                'class': 'form-control',
                'placeholder': 'Value from: ...'
            }
        )
    )
    end_value = NumberFilter(
        field_name='value',
        lookup_expr='lte',
        widget=DateInput(
            {
                'class': 'form-control',
                'placeholder': 'Value to: ...'
            }
        )
    )
    start_date = DateFilter(
        field_name='date',
        lookup_expr='gte',
        widget=DateInput(
            {
                'class': 'form-control',
                'placeholder': 'Date from: YYYY-MM-DD'
            }
        )
    )
    end_date = DateFilter(
        field_name='date',
        lookup_expr='lte',
        widget=DateInput(
            {
                'class': 'form-control',
                'placeholder': 'Date to: YYYY-MM-DD'
            }
        )
    )

    class Meta:
        model = Expenses
        fields = '__all__'


class IncomeFilter(django_filters.FilterSet):
    name = CharFilter(
        field_name='name',
        lookup_expr='icontains',
        widget=TextInput(
            {
                'class': 'form-control',
                'placeholder': 'Name contains ...'
            }
        )
    )
    start_value = NumberFilter(
        field_name='value',
        lookup_expr='gte',
        widget=DateInput(
            {
                'class': 'form-control',
                'placeholder': 'Value from: ...'
            }
        )
    )
    end_value = NumberFilter(
        field_name='value',
        lookup_expr='lte',
        widget=DateInput(
            {
                'class': 'form-control',
                'placeholder': 'Value to: ...'
            }
        )
    )
    start_date = DateFilter(
        field_name='date',
        lookup_expr='gte',
        widget=DateInput(
            {
                'class': 'form-control',
                'placeholder': 'Date from: YYYY-MM-DD'
            }
        )
    )
    end_date = DateFilter(
        field_name='date',
        lookup_expr='lte',
        widget=DateInput(
            {
                'class': 'form-control',
                'placeholder': 'Date to: YYYY-MM-DD'
            }
        )
    )

    class Meta:
        model = Income
        fields = '__all__'
