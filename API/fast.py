from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import logging
import lightgbm as lgb

app = FastAPI()

# Set up logging
logging.basicConfig(level=logging.INFO)

# Load the LightGBM model
with open("../data/linear_regression_model.pkl", "rb") as f:
    model = pickle.load(f)

class JobData(BaseModel):
    longitude: float
    latitude: float
    housing_median_age: float
    total_rooms: float
    total_bedrooms: float
    population: float
    median_income: float

@app.get('/')
def index():
    return {'message': 'Hello, stranger, from local'}

@app.post('/predict')
def predict_job(job_data: JobData):
    try:
        data = job_data.dict()

        # Transform the data into the expected format
        features = [list(data.values())]  # Convert dict values to a list

        # Predict using the LightGBM model
        prediction = model.predict(features)[0]

        return {
            'prediction': prediction
        }

    except Exception as e:
        logging.error("Exception occurred", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
