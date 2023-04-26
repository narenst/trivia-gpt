from tests.triviagpt.conftest import client


def test_get_or_create_by_reference(client):
    """
    Check if user is created if it doesn't exist.
    """
    reference = "random_test_reference"
    response = client.get('/user/get_or_create_by_reference/' + reference)

    assert response.status_code == 200
    assert response.json['reference'] == reference

    username = response.json['username']

    new_response = client.get('/user/get_or_create_by_reference/' + reference)
    assert new_response.status_code == 200
    assert new_response.json['username'] == username


def test_get_by_username(client, test_user):
    """
    Check if user is returned by username.
    """
    response = client.get('/user/get_by_username/test_user')
    assert response.status_code == 200
    assert response.json['username'] == 'test_user'
    assert response.json['reference'] == 'test_reference'


def test_get_non_existent_user(client):
    """
    If a user does not exist with the username.
    """
    response = client.get('/user/get_by_username/non_existent_user')
    assert response.status_code == 404
    assert response.data == b'User not found.'