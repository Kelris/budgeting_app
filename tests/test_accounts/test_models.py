import pytest

from accounts.models import User


@pytest.mark.django_db
class TestModels(object):

    @pytest.fixture
    def user(self):
        return User.objects.create(
            first_name='John',
            last_name='Doe'
        )

    def test_fields_labels(self):
        labels_list = [
            ('email', 'Email address'),
        ]

        for label in labels_list:
            field_label = User._meta.get_field(label[0]).verbose_name
            assert field_label == label[1]

    def test_string_representation(self, user):
        user_str_representation = f"{user.id} - {user.username} " \
                                  f"{user.full_name}"
        assert user_str_representation == str(user)

    def test_full_name(self, user):
        assert user.full_name == 'John Doe'
