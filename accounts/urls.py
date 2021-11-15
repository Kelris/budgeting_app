from django.urls import path

from accounts.views import Login_View, RegisterView

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', Login_View.as_view(), name='login'),
    ]
