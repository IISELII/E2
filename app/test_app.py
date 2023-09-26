import requests
import json

api_url = "http://localhost:8000"

def test_api_returns_json():
    # Simuler les données d'entrées avec les types de données correcte pour notre modèle
    data = {
        "longitude": 122.5,
        "latitude": 37.7,
        "housing_median_age": 20.0,
        "total_rooms": 4000.0,
        "total_bedrooms": 800.0,
        "population": 2000.0,
        "median_income": 3.5
    }
    
    response = requests.post(f"{api_url}/predict", json=data)
    assert response.status_code == 200


def test_api_inputs_are_floats():
    # La fonction pour requêter notre api
    def send_request(input_data):
        response = requests.post(f"{api_url}/predict", json=input_data)
        return response

    # Simuler des données d'entrées avec des mauvais types de données pour notre modèle
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
        response = send_request(temp_data) # Envoyer la requète api avec les input
        assert response.status_code == 422 # On vérifie que le status_code est bien 422
        assert key in response.text # On vérifie que la key qui à été modifier est bien dans le message d'erreur
