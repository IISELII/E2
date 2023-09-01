import streamlit as st
import requests

# Streamlit UI

# Function to interact with FastAPI endpoint
def get_prediction_from_api(data):
    api_url = "http://localhost:8000"
    response = requests.post(f"{api_url}/predict", json=data)
    if response.status_code != 200:
        st.error(f"Failed to get a valid response. Status code: {response.status_code}. Content: {response.text}")
        return
    return response.json()

st.sidebar.title("Navigation")
page = st.sidebar.radio("Choisissez une page", ["Accueil", "Prédictions", "Visualisation"])

if page == "Accueil":
    st.title("Bienvenu sur notre app !")
    st.write('Naviguez vers la page "Prédictions" pour prédire avec votre modèle LightGBM !')
    st.write('Ou allez à la page "Visualisation" pour voir des graphes intéressants.')

elif page == "Prédictions":
    st.title("Faites une prédiction avec votre modèle LightGBM")

    # Placeholder: Supposez que vous avez trois caractéristiques
    # Placeholder: Supposez que vous avez les caractéristiques suivantes
    longitude = float(st.number_input("longitude:", min_value=0.0))
    latitude = float(st.number_input("latitude:", min_value=0.0))
    housing_median_age = float(st.number_input("housing median age:", min_value=0.0))
    total_rooms = float(st.number_input("total rooms", min_value=0.0))
    total_bedrooms = float(st.number_input("total bedrooms", min_value=0.0))
    population = float(st.number_input("population", min_value=0.0))
    households = float(st.number_input("households", min_value=0.0))
    median_income = float(st.number_input("median income", min_value=0.0))
    ocean_proximity_1H_ocean = float(st.number_input("ocean proximity <1H_ocean", min_value=0.0))
    ocean_proximity_INLAND = float(st.number_input("ocean proximity INLAND", min_value=0.0))
    ocean_proximity_ISLAND = float(st.number_input("ocean proximity ISLAND", min_value=0.0))
    ocean_proximity_NEAR_BAY = float(st.number_input("ocean proximity NEAR BAY", min_value=0.0))
    ocean_proximity_NEAR_OCEAN = float(st.number_input("ocean proximity NEAR OCEAN", min_value=0.0))


    # Prediction button
    if st.button("Prédire"):
        data = {
            "longitude": longitude,
            "latitude": latitude,
            "housing_median_age": housing_median_age,
            "total_rooms": total_rooms,
            "total_bedrooms": total_bedrooms,
            "population": population,
            "households": households,
            "median_income": median_income,
            "ocean_proximity_1H_ocean": ocean_proximity_1H_ocean,
            "ocean_proximity_INLAND": ocean_proximity_INLAND,
            "ocean_proximity_ISLAND": ocean_proximity_ISLAND,
            "ocean_proximity_NEAR_BAY": ocean_proximity_NEAR_BAY,
            "ocean_proximity_NEAR_OCEAN": ocean_proximity_NEAR_OCEAN
        }
        result = get_prediction_from_api(data)
        if result and 'prediction' in result:
            st.write(f"Prédiction: {result['prediction']}")
        else:
            st.write("Echec de la prédiction.")

elif page == "Visualisation":
    st.title("Visualisation des données")
    st.write("Ici, vous pouvez ajouter des graphes pour analyser vos données.")
    st.subheader("Sous-titre pour votre graphique")
    # Exemple de graphique, à remplacer par le vôtre
    # chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    # st.line_chart(chart_data)
