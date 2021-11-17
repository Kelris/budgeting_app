from django.urls import resolve

from budget import views


class TestUrls(object):
    def test_list_urls_is_resolved(self):
        """Checks if the URL matches the view."""
        test_urls_list = [
            ('/budget/', views.IndexView),

            ('/budget/categories_list/', views.CategoriesListView),
            ('/budget/category_create/', views.CategoryCreateView),
            ('/budget/category_update/1', views.CategoryUpdateView),
            ('/budget/category_delete/1', views.CategoryDeleteView),

            ('/budget/expenses_list/', views.ExpensesListView),
            ('/budget/expense_create/', views.ExpenseCreateView),
            ('/budget/expense_update/1', views.ExpenseUpdateView),
            ('/budget/expense_delete/1', views.ExpenseDeleteView),

            ('/budget/income_list/', views.IncomeListView),
            ('/budget/income_create/', views.IncomeCreateView),
            ('/budget/income_update/1', views.IncomeUpdateView),
            ('/budget/income_delete/1', views.IncomeDeleteView),
        ]

        for url in test_urls_list:
            assert resolve(url[0]).func.view_class == url[1]
