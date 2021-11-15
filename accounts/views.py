from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import LoginForm, RegisterForm


class RegisterView(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/register.html'


class Login_View(LoginRequiredMixin, LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'
