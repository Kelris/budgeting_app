import pytest
from rest_framework.test import APITestCase

from accounts.models import User
from budget.models import Category, Expenses, Income


@pytest.mark.django_db
class TestAPIUrls(APITestCase):

    def test_url_addresses(self):
        user = User.objects.create(
            first_name='John',
            last_name='Doe',
            email='test@gmail.com',
            password='testTEST**',
            username='test_user'
        )
        category = Category.objects.create(
            id=1, name='food', owner=user)
        Expenses.objects.create(
            id=1, name='apple', value=1.5, category=category, date='2015-04-26',)  # noqa
        Income.objects.create(
            id=1, name='salary', value=1000, date='2015-04-26', owner=user,)
        url_addresses = [
            'http://testserver/api/categories_list',
            'http://testserver/api/category_update/1',

            'http://testserver/api/expenses_list',
            'http://testserver/api/expense_update/1',

            'http://testserver/api/income_list',
            'http://testserver/api/income_update/1',

        ]

        self.client.force_authenticate(user)
        for url in url_addresses:
            response = self.client.get(url)
            assert response.status_code == 200
