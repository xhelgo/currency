def test_index(client):
    response = client.get('/')
    assert response.status_code == 200


def test_rate_list(client):
    response = client.get('/currency/rates/list/')
    assert response.status_code == 200


def test_login(client):
    response = client.get('/auth/login/')
    assert response.status_code == 200


def test_sign_up(client):
    response = client.get('/account/signup/')
    assert response.status_code == 200
