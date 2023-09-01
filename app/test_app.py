import requests
import json

api_url = "http://localhost:8000"

def test_api_returns_json():
    # Simuler les données d'entrées
    data = {
        "longitude": 122.5,
        "latitude": 37.7,
        "housing_median_age": 20.0,
        "total_rooms": 4000.0,
        "total_bedrooms": 800.0,
        "population": 2000.0,
        "median_income": 3.5,
    }
    
    response = requests.post(f"{api_url}/predict", json=data)
    assert response.status_code == 200
    # Si la réponse est valide : 
    try:    
        response_content = response.json()
        assert isinstance(response_content, dict)
    
    # Sinon :
    except json.JSONDecodeError:
        raise AssertionError("Erreur lors du décodage de la réponse API en tant que JSON ")

def test_api_inputs_are_floats():
    # La fonction pour requêter une api
    def send_request(input_data):
        response = requests.post(f"{api_url}/predict", json=input_data)
        return response

    # Simuler des données d'entrées
    base_data = {
        "longitude": 122.5,
        "latitude": 37.7,
        "housing_median_age": 20.0,
        "total_rooms": 4000.0,
        "total_bedrooms": 800.0,
        "population": 2000.0,
        "median_income": 3.5,
    }

    for key in base_data:
        temp_data = dict(base_data)  # Créer une copie des données
        temp_data[key] = "not_a_float"  # Remplacer une valeur avec un string
        response = send_request(temp_data)
        assert response.status_code != 200
        assert key in response.text
