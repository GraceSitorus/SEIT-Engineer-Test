import requests


def test_get_all_course():
    response = requests.get('https://skillacademy.com/api/skillacademy/discovery/search')
    data = response.json().get('data')
    assert response.status_code == 200
    assert len(data) > 5

def test_get_one_course():
    response = requests.get('https://skillacademy.com/api/skillacademy/discovery/search')
    assert response.status_code == 200
    data = response.json()
    assert data["basePrice"] == "300000"