import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
Token = 'token'

Headers = {'Content-Type': 'application/json', 'trainer_token': Token}
id = 193

def test_status_code():
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id': id}, headers=Headers)
    assert response.status_code == 200
   
def test_part_of_response():
    response = requests.get(url=f'{URL}/trainers', params={'trainer_id': id}, headers=Headers)
    assert response.json() ['data'][0]['trainer_name'] == 'Vendetta'

