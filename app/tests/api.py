from currency.models import Rate, ContactUs


def test_get_api_rate_list(api_client):
    response = api_client.get('/api/currency/rates/')
    assert response.status_code == 200


def test_post_api_rates_list(api_client):
    response = api_client.post('/api/currency/rates/')
    assert response.status_code == 400
    assert response.json() == {
        "buy": [
            "This field is required."
        ],
        "sell": [
            "This field is required."
        ],
        "source": [
            "This field is required."
        ]
    }


def test_post_api_rate_create(api_client):
    data = {
        "buy": 39.90,
        "sell": 40.11,
        "source": 1
    }
    response = api_client.post('/api/currency/rates/', data=data)
    assert response.status_code == 201


def test_post_api_rate_update(api_client):
    data = {
        "id": 1,
        "buy": 39.90,
        "sell": 40.11,
        "source": 1
    }
    response = api_client.put('/api/currency/rates/1/', data=data)
    assert response.status_code == 200


def test_delete_api_rate(api_client):
    response = api_client.delete('/api/currency/rates/50/')
    assert response.status_code == 204
    assert not Rate.objects.filter(id=50).exists()


def test_get_api_sources_list(api_authenticated_client):
    response = api_authenticated_client.get('/api/currency/sources/')
    assert response.status_code == 200


def test_get_api_sources_list_anonymous(api_client):
    response = api_client.get('/api/currency/sources/')
    assert response.status_code == 401


def test_get_api_contactus_list_anonymous(api_client):
    response = api_client.get('/api/currency/contactus/')
    assert response.status_code == 401


def test_get_api_contactus_list_superuser(api_superuser_client):
    response = api_superuser_client.get('/api/currency/contactus/')
    assert response.status_code == 200


def test_post_api_contactus_list(api_client):
    response = api_client.post('/api/currency/contactus/')
    assert response.status_code == 400
    assert response.json() == {
        'email_from': ['This field is required.'],
        'message': ['This field is required.'],
        'name': ['This field is required.'],
        'subject': ['This field is required.']
    }


def test_post_api_contactus_create(api_client):
    data = {
        'email_from': 'email@email.com',
        'message': 'This field is required.',
        'name': 'This field is required.',
        'subject': 'This field is required.'
    }
    response = api_client.post('/api/currency/contactus/', data=data)
    assert response.status_code == 201


def test_put_api_contactus_update(api_superuser_client):
    data = {
        'id': 1,
        'email_from': 'updated_email@email.com',
        'message': 'This field is required.',
        'name': 'This field is required.',
        'subject': 'This field is required.'
    }
    response = api_superuser_client.put('/api/currency/contactus/1/', data=data)
    assert response.status_code == 200


def test_delete_api_contactus(api_superuser_client):
    response = api_superuser_client.delete('/api/currency/contactus/1/')
    assert response.status_code == 204
    assert not ContactUs.objects.filter(id=1).exists()
