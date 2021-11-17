from django.urls import resolve

from accounts.views import Login_View, RegisterView


class TestUrls(object):
    def test_list_urls_is_resolved(self):
        """Checks if the URL matches the view."""
        test_urls_list = [
            ('/accounts/register/', RegisterView),
            ('/accounts/login/', Login_View),
        ]

        for url in test_urls_list:
            assert resolve(url[0]).func.view_class == url[1]
