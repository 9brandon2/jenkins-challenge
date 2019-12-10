import pytest
import requests
from build import Birthyear
import json

# Test GET
def test_get_404():
    user = "brandon"
    bad_user = "chris"
    birth_data = {user: 1992}
    by = Birthyear(birth_data=birth_data)
    assert by.get(bad_user) == 404

def test_happy_validate_key():
    user = "brandon"
    birth_data = {user: 1992}
    by = Birthyear(birth_data=birth_data)
    assert (by.get(user)) == ({user: 1992}, 200)

# Test POST
def test_happy_32_bit_int():
    user = "test_32_bit"
    birth_year = "1992"
    payload = {
        'data': birth_year
    }
    by = Birthyear()
    response = requests.post('http://0.0.0.0:5000/%s' % user, data=payload)
    assert response.status_code == 204
    

def test_sad_32_bit_int():
    user = "test_32_bit"
    unhappy_bit_size = "12312123123"
    payload = {
        'data': unhappy_bit_size
    }
    by = Birthyear()
    response = requests.post('http://0.0.0.0:5000/%s' % user, data=payload)
    assert response.status_code == 400

# Test delete
def test_delete_user():
    user = "new_user"
    birth_year = 1992
    birth_data = {user: birth_year}
    by = Birthyear(birth_data=birth_data)
    user_list = requests.get('http://0.0.0.0:5000/%s' % user)
    response = json.loads(user_list.text)
    uploaded_user = list(response.keys())[0]
    response = by.delete(user)
    assert response == ({}, 204)

def test_unhappy_delete():
    user = "new_user"
    wrong_user = "wrong_user"
    birth_year = 1992
    birth_data = {user: birth_year}
    by = Birthyear(birth_data=birth_data)
    user_list = requests.get('http://0.0.0.0:5000/%s' % user)
    response = json.loads(user_list.text)
    uploaded_user = list(response.keys())[0]
    response = by.delete(wrong_user)
    assert response == 400
