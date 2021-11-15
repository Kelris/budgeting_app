from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import RegisterForm


class RegisterView(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('budget:index')
    template_name = 'accounts/register.html'
