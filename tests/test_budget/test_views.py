import pytest
from django.test.client import Client

from accounts.models import User
from budget.models import Category, Expenses, Income


@pytest.fixture()
def client(admin_user):
    client = Client()
    client.force_login(admin_user)
    return client


@pytest.fixture
def user():
    return User.objects.create()


@pytest.fixture(autouse=True)
def category(user):
    return Category.objects.create(
        id=1,
        name='food',
        owner=user,
    )


@pytest.fixture(autouse=True)
def expenses(category):
    return Expenses.objects.create(
        id=1,
        name='apple',
        value=1.5,
        category=category,
        date='2015-04-26',
    )


@pytest.fixture(autouse=True)
def income(user):
    return Income.objects.create(
        id=1,
        name='salary',
        value=1000,
        date='2015-04-26',
        owner=user,
    )


@pytest.mark.django_db
class TestViews(object):

    @pytest.mark.parametrize('url_pattern', [
        '/budget/',

        '/budget/categories_list/',
        '/budget/category_create/',
        '/budget/category_update/1',
        '/budget/category_delete/1',

        '/budget/expenses_list/',
        '/budget/expense_create/',
        '/budget/expense_update/1',
        '/budget/expense_delete/1',

        '/budget/income_list/',
        '/budget/income_create/',
        '/budget/income_update/1',
        '/budget/income_delete/1',
    ])
    def test_url(self, url_pattern, client):
        response = client.get(url_pattern)
        assert response.status_code == 200

    @pytest.mark.parametrize('url_pattern, template_name', [
        ('/budget/', 'budget/index.html'),

        ('/budget/categories_list/', 'budget/categories_list.html'),
        ('/budget/category_create/', 'budget/category_create.html'),
        ('/budget/category_update/1', 'budget/category_update.html'),
        ('/budget/category_delete/1', 'budget/category_delete.html'),

        ('/budget/expenses_list/', 'budget/expenses_list.html'),
        ('/budget/expense_create/', 'budget/expense_create.html'),
        ('/budget/expense_update/1', 'budget/expense_update.html'),
        ('/budget/expense_delete/1', 'budget/expense_delete.html'),

        ('/budget/income_list/', 'budget/income_list.html'),
        ('/budget/income_create/', 'budget/income_create.html'),
        ('/budget/income_update/1', 'budget/income_update.html'),
        ('/budget/income_delete/1', 'budget/income_delete.html'),
    ])
    def test_template(self, client, url_pattern, template_name):
        response = client.get(url_pattern)
        assert template_name in (t.name for t in response.templates)
