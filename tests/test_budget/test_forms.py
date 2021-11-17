from datetime import date

import pytest

from accounts.models import User
from budget.forms import CategoryForm, ExpenseForm, IncomeForm


@pytest.fixture
def user():
    return User.objects.create()


@pytest.mark.django_db
class TestCategoryForm(object):

    def test_form_fields(self):
        form = CategoryForm()
        form_fields = ['name', 'owner']
        assert [k for k in form.fields.keys()] == form_fields

    def test_valid_data(self, user):
        form = CategoryForm(data={
            'name': 'food',
            'owner': user,
        })
        assert form.is_valid()

    def test_required_fields(self):
        data = {
            'name': '',
            'owner': '',
        }

        form = CategoryForm(data)

        for key in data:
            assert form.errors[key] == ['This field is required.']

    def test_widget_attrs(self):
        form = CategoryForm()
        widget_attrs_list = [
            ('name', {
                'class': 'form-control',
                'maxlength': '40',
                'placeholder': 'Name'
            }),
        ]

        for line in widget_attrs_list:
            assert form.fields[line[0]].widget.attrs == line[1]


@pytest.mark.django_db
class TestExpenseForm(object):

    def test_form_fields(self):
        form = ExpenseForm()
        form_fields = ['name', 'value', 'category', 'date']
        assert [k for k in form.fields.keys()] == form_fields

    def test_required_fields(self):
        data = {
            'value': '',
            'category': '',
            'date': '',
        }

        form = ExpenseForm(data)

        for key in data:
            assert form.errors[key] == ['This field is required.']

    def test_widget_attrs(self):
        form = ExpenseForm()
        widget_attrs_list = [
            ('name', {
                'class': 'form-control',
                'maxlength': '40',
                'placeholder': 'Name (optional)'
            }),
            ('value', {
                'class': 'form-control',
                'step': '0.01',
                'placeholder': 'Value'
            }),
            ('category', {
                'class': 'form-control',
                'placeholder': 'Category'
            }),
            ('date', {
                'class': 'form-control',
                'placeholder': 'Date'
            }),
        ]

        for line in widget_attrs_list:
            assert form.fields[line[0]].widget.attrs == line[1]


@pytest.mark.django_db
class TestIncomeForm(object):

    def test_form_fields(self):
        form = IncomeForm()
        form_fields = ['name', 'value', 'date', 'owner']
        assert [k for k in form.fields.keys()] == form_fields

    def test_valid_data(self, user):
        form = IncomeForm(data={
            'owner': user,
            'value': 20,
            'date': date.today(),
        })
        assert form.is_valid()

    def test_required_fields(self):
        data = {
            'owner': '',
            'value': '',
            'date': '',
        }

        form = IncomeForm(data)

        for key in data:
            assert form.errors[key] == ['This field is required.']

    def test_widget_attrs(self):
        form = IncomeForm()
        widget_attrs_list = [
            ('name', {
                'class': 'form-control',
                'maxlength': '40',
                'placeholder': 'Name (optional)'
            }),
            ('value', {
                'class': 'form-control',
                'step': '0.01',
                'placeholder': 'Value'
            }),
            ('date', {
                'class': 'form-control',
                'placeholder': 'Date'
            }),
        ]

        for line in widget_attrs_list:
            assert form.fields[line[0]].widget.attrs == line[1]
