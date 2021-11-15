from django.contrib.auth import views as auth_views
from django.urls import path

from accounts.views import Login_View, RegisterView

app_name = 'accounts'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', Login_View.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='accounts/logout.html'), name="logout"),
    ]
