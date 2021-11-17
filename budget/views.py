from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, TemplateView,
                                  UpdateView, ListView)
from django_filters.views import FilterView

from budget.filters import CategoriesFilter, ExpensesFilter, IncomeFilter
from budget.forms import CategoryForm, ExpenseForm, IncomeForm
from budget.models import Category, Expenses, Income


class IndexView(TemplateView):
    template_name = 'budget/index.html'


class CategoriesListView(FilterView, LoginRequiredMixin):
    model = Category
    filterset_class = CategoriesFilter
    paginate_by = 10
    template_name = 'budget/categories_list.html'

    def get_queryset(self):
        return Category.objects.order_by('id').reverse().filter(
            owner=self.request.user)


class CategoryCreateView(CreateView, LoginRequiredMixin):
    model = Category
    form_class = CategoryForm
    template_name = 'budget/category_create.html'
    success_url = reverse_lazy('budget:expense_create')


class CategoryUpdateView(UpdateView, LoginRequiredMixin):
    model = Category
    form_class = CategoryForm
    template_name = 'budget/category_update.html'
    success_url = reverse_lazy('budget:expense_create')

    def get_object(self):
        object_id = self.kwargs.get("id")
        return get_object_or_404(Category, id=object_id)

    def get_queryset(self):
        return Category.objects.filter(owner=self.request.user)

    def dispatch(self, request, *args, **kwargs):
        handler = super().dispatch(request, *args, **kwargs)
        user = request.user
        category = self.get_object()
        if not (category.owner == user or user.is_superuser):
            raise PermissionDenied
        return handler


class CategoryDeleteView(DeleteView, LoginRequiredMixin):
    model = Category
    form_class = CategoryForm
    template_name = 'budget/category_delete.html'
    success_url = reverse_lazy('budget:expense_create')

    def get_object(self):
        object_id = self.kwargs.get("id")
        return get_object_or_404(Category, id=object_id)

    def get_queryset(self):
        return Category.objects.filter(owner=self.request.user)

    def dispatch(self, request, *args, **kwargs):
        handler = super().dispatch(request, *args, **kwargs)
        user = request.user
        category = self.get_object()
        if not (category.owner == user or user.is_superuser):
            raise PermissionDenied
        return handler


class ExpensesListView(FilterView, LoginRequiredMixin):
    model = Expenses
    filterset_class = ExpensesFilter
    paginate_by = 10
    template_name = 'budget/expenses_list.html'

    def get_queryset(self):
        return Expenses.objects.order_by('date').reverse().filter(
            category__owner=self.request.user
        )


class ExpenseCreateView(CreateView, LoginRequiredMixin):
    model = Expenses
    form_class = ExpenseForm
    template_name = 'budget/expense_create.html'
    success_url = reverse_lazy('budget:expenses_list')

    def get_form_kwargs(self):
        kwargs = super(ExpenseCreateView, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class ExpenseUpdateView(UpdateView, LoginRequiredMixin):
    model = Expenses
    form_class = ExpenseForm
    template_name = 'budget/expense_update.html'
    success_url = reverse_lazy('budget:expenses_list')

    def get_object(self):
        object_id = self.kwargs.get("id")
        return get_object_or_404(Expenses, id=object_id)

    def dispatch(self, request, *args, **kwargs):
        handler = super().dispatch(request, *args, **kwargs)
        user = request.user
        expense = self.get_object()
        if not (expense.category.owner == user or user.is_superuser):
            raise PermissionDenied
        return handler


class ExpenseDeleteView(DeleteView, LoginRequiredMixin):
    model = Expenses
    form_class = ExpenseForm
    template_name = 'budget/expense_delete.html'
    success_url = reverse_lazy('budget:expenses_list')

    def get_object(self):
        object_id = self.kwargs.get("id")
        return get_object_or_404(Expenses, id=object_id)

    def dispatch(self, request, *args, **kwargs):
        handler = super().dispatch(request, *args, **kwargs)
        user = request.user
        expense = self.get_object()
        if not (expense.category.owner == user or user.is_superuser):
            raise PermissionDenied
        return handler


class IncomeListView(FilterView, LoginRequiredMixin):
    model = Income
    filterset_class = IncomeFilter
    paginate_by = 10
    template_name = 'budget/income_list.html'

    def get_queryset(self):
        return Income.objects.order_by('date').reverse().filter(
            owner=self.request.user)


class IncomeCreateView(CreateView, LoginRequiredMixin):
    model = Income
    form_class = IncomeForm
    template_name = 'budget/income_create.html'
    success_url = reverse_lazy('budget:income_list')


class IncomeUpdateView(UpdateView, LoginRequiredMixin):
    model = Income
    form_class = IncomeForm
    template_name = 'budget/income_update.html'
    success_url = reverse_lazy('budget:income_list')

    def get_object(self):
        object_id = self.kwargs.get("id")
        return get_object_or_404(Income, id=object_id)

    def get_queryset(self):
        return Income.objects.filter(owner=self.request.user)

    def dispatch(self, request, *args, **kwargs):
        handler = super().dispatch(request, *args, **kwargs)
        user = request.user
        income = self.get_object()
        if not (income.owner == user or user.is_superuser):
            raise PermissionDenied
        return handler


class IncomeDeleteView(DeleteView, LoginRequiredMixin):
    model = Income
    form_class = IncomeForm
    template_name = 'budget/income_delete.html'
    success_url = reverse_lazy('budget:income_list')

    def get_object(self):
        object_id = self.kwargs.get("id")
        return get_object_or_404(Income, id=object_id)

    def get_queryset(self):
        return Income.objects.filter(owner=self.request.user)

    def dispatch(self, request, *args, **kwargs):
        handler = super().dispatch(request, *args, **kwargs)
        user = request.user
        income = self.get_object()
        if not (income.owner == user or user.is_superuser):
            raise PermissionDenied
        return handler
