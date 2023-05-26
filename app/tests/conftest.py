import pytest
from django.core.management import call_command
from rest_framework.test import APIClient


@pytest.fixture(autouse=True, scope="function")
def enable_db_access_for_all_tests(db):
    """
    give access to database for all tests
    """


@pytest.fixture()
def api_client():
    client = APIClient()
    yield client


@pytest.fixture()
def api_authenticated_client(django_user_model):
    client = APIClient()
    user = django_user_model.objects.get(username='authenticated_test_user')
    client.force_authenticate(user=user)
    yield client


@pytest.fixture()
def api_superuser_client(django_user_model):
    client = APIClient()
    user = django_user_model.objects.get(username='super_test_user')
    client.force_authenticate(user=user)
    yield client


@pytest.fixture(autouse=True, scope="session")
def load_fixtures(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        fixtures = (
            'sources.json',
            'rates.json',
            'users.json',
            'contact_us.json'
        )
        for fixture in fixtures:
            call_command('loaddata', f'app/tests/fixtures/{fixture}')
