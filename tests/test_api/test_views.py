from collections import OrderedDict
from datetime import date

import pytest
from rest_framework.test import (APIRequestFactory, APITestCase,
                                 force_authenticate)

from accounts.models import User
from api.views import (CategoryDetailUpdateDeleteAPIView,
                       ExpenseDetailUpdateDeleteAPIView,
                       IncomeDetailUpdateDeleteAPIView)
from budget.models import Category, Expenses, Income


@pytest.mark.django_db
class TestCategoriesViews(APITestCase):
    factory = APIRequestFactory()

    def test_create_and_list(self):
        user = User.objects.create(
            first_name='John',
            last_name='Doe',
            email='test@gmail.com',
            password='testTEST**',
            username='test_user',
        )

        self.client.force_authenticate(user)
        response = self.client.post(
            'http://testserver/api/categories_list',
            {
                "name": "food",
                "owner": "user",
            })

        assert Category.objects.count() == 1
        assert Category.objects.get().name == 'food'
        assert Category.objects.get().owner.username == 'test_user'

        response = self.client.get('http://testserver/api/categories_list')

        assert response.status_code == 200
        assert response.data['results'] == [
            OrderedDict([('id', 1), ('name', 'food')])]

    def test_detail_update_delete(self):
        user = User.objects.create(
            first_name='John',
            last_name='Doe',
            email='test@gmail.com',
            password='testTEST**',
            username='test_user',
        )
        Category.objects.create(
            id=1,
            name='food',
            owner=user,
        )
        view = CategoryDetailUpdateDeleteAPIView.as_view()

        request = self.factory.get('http://testserver/api/category_update/1')
        force_authenticate(request, user=user)
        response = view(request, id=1)

        assert response.data == {'id': 1, 'name': 'food'}


class TestExpensesViews(APITestCase):
    factory = APIRequestFactory()

    def test_create_and_list(self):
        user = User.objects.create(
            first_name='John',
            last_name='Doe',
            email='test@gmail.com',
            password='testTEST**',
            username='test_user',
        )
        Category.objects.create(
            id=1,
            name='food',
            owner=user,
        )

        self.client.force_authenticate(user)
        self.client.post(
            'http://testserver/api/expenses_list',
            {
                'name': 'apple',
                'value': 20,
                'category': 1,
                'date': date.today(),
                'owner': 'test_user',
            })

        assert Expenses.objects.count() == 1
        assert Expenses.objects.get().name == 'apple'
        assert Expenses.objects.get().category.owner == user

        response = self.client.get('http://testserver/api/expenses_list')

        assert response.status_code == 200
        assert response.data['results'] == [
            OrderedDict([('id', 1), ('name', 'apple'), ('value', '20.00'),
                         ('category', 1), ('date', '2021-11-18')])
        ]

    def test_detail_update_delete(self):
        user = User.objects.create(
            first_name='John',
            last_name='Doe',
            email='test@gmail.com',
            password='testTEST**',
            username='test_user',
        )
        category = Category.objects.create(
            id=1,
            name='food',
            owner=user,
        )
        Expenses.objects.create(
            id=1,
            name='apple',
            value=1.5,
            category=category,
            date='2015-04-26',
        )
        view = ExpenseDetailUpdateDeleteAPIView.as_view()

        request = self.factory.get('http://testserver/api/expense_update/1')
        force_authenticate(request, user=user)
        response = view(request, id=1)

        assert response.data == {
            'id': 1, 'name': 'apple', 'value': '1.50',
            'category': 1, 'date': '2015-04-26'
        }


class TestIncomeViews(APITestCase):
    factory = APIRequestFactory()

    def test_create_and_list(self):
        user = User.objects.create(
            first_name='John',
            last_name='Doe',
            email='test@gmail.com',
            password='testTEST**',
            username='test_user',
        )

        self.client.force_authenticate(user)
        self.client.post(
            'http://testserver/api/income_list',
            {
                'name': 'food',
                'value': 20,
                'date': date.today(),
                'owner': 'test_user',
            })

        assert Income.objects.count() == 1
        assert Income.objects.get().name == 'food'
        assert Income.objects.get().owner.username == 'test_user'

        response = self.client.get('http://testserver/api/income_list')

        assert response.status_code == 200
        assert response.data['results'] == [
            OrderedDict([('id', 1), ('name', 'food'), ('value', '20.00'),
                         ('date', '2021-11-18')])]

    def test_detail_update_delete(self):
        user = User.objects.create(
            first_name='John',
            last_name='Doe',
            email='test@gmail.com',
            password='testTEST**',
            username='test_user',
        )
        Income.objects.create(
            id=1,
            name='salary',
            value=1000,
            date=date.today(),
            owner=user,
        )
        view = IncomeDetailUpdateDeleteAPIView.as_view()

        request = self.factory.get('http://testserver/api/income_update/1')
        force_authenticate(request, user=user)
        response = view(request, id=1)

        assert response.data == {
            'id': 1, 'name': 'salary', 'value': '1000.00',
            'date': '2021-11-18'
        }
