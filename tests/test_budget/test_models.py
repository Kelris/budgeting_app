import pytest

from accounts.models import User
from budget.models import Category, Expenses, Income


@pytest.fixture
def user():
    return User.objects.create()


@pytest.fixture
def category(user):
    return Category.objects.create(
        name='food',
        owner=user,
    )


@pytest.fixture
def expenses(category):
    return Expenses.objects.create(
        name='apple',
        value=1.5,
        category=category,
        date='2015-04-26',
    )


@pytest.fixture
def income(user):
    return Income.objects.create(
        name='salary',
        value=1000,
        date='2015-04-26',
        owner=user,
    )


@pytest.mark.django_db
class TestModels(object):

    def test_fields_labels(self):
        category_labels_list = [
            ('name', 'name'),
            ('owner', 'owner'),
        ]
        expenses_labels_list = [
            ('name', 'name'),
            ('value', 'value'),
            ('category', 'category'),
            ('date', 'date'),
        ]
        income_labels_list = [
            ('name', 'name'),
            ('value', 'value'),
            ('date', 'date'),
            ('owner', 'owner'),
        ]

        for label in category_labels_list:
            field_label = Category._meta.get_field(label[0]).verbose_name
            assert field_label == label[1]

        for label in expenses_labels_list:
            field_label = Expenses._meta.get_field(label[0]).verbose_name
            assert field_label == label[1]

        for label in income_labels_list:
            field_label = Income._meta.get_field(label[0]).verbose_name
            assert field_label == label[1]

    @pytest.mark.parametrize('model_obj', [Category, Expenses, Income])
    def test_name_parameters(self, model_obj):
        max_length = model_obj._meta.get_field('name').max_length
        assert max_length == 40

    @pytest.mark.parametrize('model_obj', [Expenses, Income])
    def test_value_parameters(self, model_obj):
        max_digits = model_obj._meta.get_field('value').max_digits
        decimal_places = model_obj._meta.get_field('value').decimal_places
        assert max_digits == 10
        assert decimal_places == 2

    def test_string_representation(self, category, expenses, income):
        category_str_representation = category.name
        expenses_str_representation = f"{expenses.category} {expenses.value}" \
                                      f" zł {expenses.name}"
        income_str_representation = f"{income.value} zł {income.name}"
        assert category_str_representation == str(category)
        assert expenses_str_representation == str(expenses)
        assert income_str_representation == str(income)

    def test_expenses_category_relation(self, category, expenses):
        assert expenses.category.name == 'food'
