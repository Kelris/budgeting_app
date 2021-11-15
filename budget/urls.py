from django.urls import path

from . import views

app_name = 'budget'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path('categories_list/', views.CategoriesListView.as_view(), name='categories_list'),  # noqa
    path('category_create/', views.CategoryCreateView.as_view(), name='category_create'),  # noqa
    path('category_update/<int:id>', views.CategoryUpdateView.as_view(), name='category_update'),  # noqa
    path('category_delete/<int:id>', views.CategoryDeleteView.as_view(), name='category_delete'),  # noqa

    path('expenses_list/', views.ExpensesListView.as_view(), name='expenses_list'),  # noqa
    path('expense_create/', views.ExpenseCreateView.as_view(), name='expense_create'),  # noqa
    path('expense_update/<int:id>', views.ExpenseUpdateView.as_view(), name='expense_update'),  # noqa
    path('expense_delete/<int:id>', views.ExpenseDeleteView.as_view(), name='expense_delete'),  # noqa

    path('income_list/', views.IncomeListView.as_view(), name='income_list'),
    path('income_create/', views.IncomeCreateView.as_view(), name='income_create'),  # noqa
    path('income_update/<int:id>', views.IncomeUpdateView.as_view(), name='income_update'),  # noqa
    path('income_delete/<int:id>', views.IncomeDeleteView.as_view(), name='income_delete'),  # noqa
]
