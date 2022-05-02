from http import client
from os import access
import pytest
from requests import request
from rest_framework import status
from rest_framework.test import APIClient, APIRequestFactory


@pytest.mark.django_db
def test_register():
    client = APIClient()
    data = {
        "email": "rivaldo@teste.com",
        "username": "rivaldopedro",
        "first_name": "rivaldo",
        "last_name": "agripino",
        "password": "123",
    }
    response = client.post('/api/register/', data, format='json')
    assert response.status_code == 200

@pytest.mark.django_db
def test_login_fail():
    client = APIClient()
    data = {
        "username": "rivaldopedro",
        "password": "123",
    }
    response = client.post('/api/token/', data, format='json')
    assert response.data == {
    "detail": "No active account found with the given credentials"
}

@pytest.mark.django_db
def test_login():
    client = APIClient()
    response = client.post('/api/token/', format='json')
    client.force_authenticate(response, token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjUxNDYxNTA5LCJpYXQiOjE2NTE0NTc5MDksImp0aSI6IjQ0YjRhZDMzNGU5NDQwYzg5MmNjZDQ0MGRlN2FhM2NiIiwidXNlcl9pZCI6MX0.RGsKPm9EcLwCBq4myf3u-kN9mDCde4texCb1eZ68FdI")
    assert response.data != None

@pytest.mark.django_db
def test_healthcheck():
    client = APIClient()
    client.force_authenticate()
    response = client.post('/api/healthcheck/', format='json')
    assert response.data != None
    
