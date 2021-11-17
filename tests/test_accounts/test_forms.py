import pytest

from accounts.forms import LoginForm, RegisterForm
from accounts.models import User


@pytest.fixture
def user():
    return User.objects.create()


@pytest.mark.django_db
class TestRegisterForm(object):

    def test_form_fields(self):
        form = RegisterForm()
        form_fields = ['username', 'email', 'password1', 'password2']
        assert [k for k in form.fields.keys()] == form_fields

    def test_valid_data(self, user):
        form = RegisterForm(data={
            'username': 'test_user',
            'email': 'test@gmail.com',
            'password1': 'testTEST**',
            'password2': 'testTEST**',
        })
        assert form.is_valid()

    def test_required_fields(self):
        data = {
            'username': '',
            'email': '',
            'password1': '',
            'password2': '',
        }

        form = RegisterForm(data)

        for key in data:
            assert form.errors[key] == ['This field is required.']

    def test_widget_attrs(self):
        form = RegisterForm()
        widget_attrs_list = [
            ('username', {
                'autofocus': True,
                'maxlength': '150',
                'class': 'form-control',
                'placeholder': 'Username'
            }),
            ('email', {
                'class': 'form-control',
                'maxlength': '254',
                'placeholder': 'Email'
            }),
            ('password1', {
                'autocomplete': 'new-password',
                'class': 'form-control',
                'placeholder': 'Password'
            }),
            ('password2', {
                'autocomplete': 'new-password',
                'class': 'form-control',
                'placeholder': 'Password confirmation'
            }),
        ]

        for line in widget_attrs_list:
            assert form.fields[line[0]].widget.attrs == line[1]


@pytest.mark.django_db
class TestLoginForm(object):

    def test_form_fields(self):
        form = LoginForm()
        form_fields = ['username', 'password']
        assert [k for k in form.fields.keys()] == form_fields

    def test_widget_attrs(self):
        form = LoginForm()
        widget_attrs_list = [
            ('username', {
                'autocapitalize': 'none',
                'autocomplete': 'username',
                'autofocus': True,
                'class': 'form-control',
                'maxlength': 150,
                'placeholder': 'Username'
            }),
            ('password', {
                'autocomplete': 'current-password',
                'class': 'form-control',
                'placeholder': 'Password'
            }),
        ]

        for line in widget_attrs_list:
            assert form.fields[line[0]].widget.attrs == line[1]
