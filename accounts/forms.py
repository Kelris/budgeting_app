from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

User = get_user_model()


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254,
        help_text='Enter a valid email address',
        widget=forms.EmailInput(
            attrs={
                'class': "form-control",
                'placeholder': "Email"
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update(
            {'class': "form-control", 'placeholder': "Username"}
        )
        self.fields['password1'].widget.attrs.update(
            {'class': "form-control", 'placeholder': "Password"}
        )
        self.fields['password2'].widget.attrs.update(
            {'class': "form-control", 'placeholder': "Password confirmation"}
        )

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update(
            {'class': "form-control", 'placeholder': "Username"}
        )
        self.fields['password'].widget.attrs.update(
            {'class': "form-control", 'placeholder': "Password"}
        )
