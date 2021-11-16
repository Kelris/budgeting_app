from django.urls import path

from api import views

app_name = 'api'

urlpatterns = [
    path('categories_list', views.CategoriesListAndCreateAPIView.as_view(), name='categories_list'),  # noqa
    path('category_update/<id>', views.CategoryDetailUpdateDeleteAPIView.as_view(), name='category_update'),  # noqa

    path('expenses_list', views.ExpensesListAndCreateAPIView.as_view(), name='expenses_list'),  # noqa
    path('expense_update/<id>', views.ExpenseDetailUpdateDeleteAPIView.as_view(), name='expense_update'),  # noqa

    path('income_list', views.IncomeListAndCreateAPIView.as_view(), name='income_list'),  # noqa
    path('income_update/<id>', views.IncomeDetailUpdateDeleteAPIView.as_view(), name='income_update'),  # noqa
]
