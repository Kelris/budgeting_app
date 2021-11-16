from django import forms

from .models import Category, Expenses, Income


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Name'}
        )


class ExpenseForm(forms.ModelForm):

    class Meta:
        model = Expenses
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(owner=self.user)  # noqa

        self.fields['name'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Name (optional)'}
        )
        self.fields['value'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Value'}
        )
        self.fields['category'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Category'}
        )
        self.fields['date'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Date'}
        )


class IncomeForm(forms.ModelForm):

    class Meta:
        model = Income
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Name (optional)'}
        )
        self.fields['value'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Value'}
        )
        self.fields['date'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Date'}
        )
