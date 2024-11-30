from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from mlpredict import ml_model_predict
from dotenv import load_dotenv
from mongoDB import get_mongo_client
from weather import fetch_weather_data
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, change it to specific domains for security
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

# MongoDB setup
db = get_mongo_client()
collection = db.forecasts  

class WeatherData(BaseModel):
    cell_temp: int
    irrad: int
    predicted_power: float
    hour: int
    minute: int

@app.get("/api/update_weather/")
async def update_weather_data():
    try:
        weather_data = fetch_weather_data()
        predicted_data = ml_model_predict(weather_data)

        date_wise_data = {}
        for data in predicted_data:
            date = data['date']
            if date not in date_wise_data:
                date_wise_data[date] = []  # Initialize list for this date
            date_wise_data[date].append({
                'hours': data['hours'],
                'minutes': data['minutes'],
                'irrad': data['irrad'],
                'cell_temperature': data['cell_temperature'],
                'predicted_power': data['predicted_power']
            })

        for date, records in date_wise_data.items():
            collection.update_one(
                {"date": date},  
                {"$set": {"records": records}}, 
                upsert=True 
            )

        return {"message": "Weather data and prediction updated successfully", "data": date_wise_data}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
from fastapi import FastAPI, HTTPException
from mongoDB import get_mongo_client

app = FastAPI()

db = get_mongo_client()
collection = db.forecasts  

@app.get("/api/get_all_data/")
async def get_all_weather_data():
    try:
        documents = list(collection.find({}))

        if not documents:
            raise HTTPException(status_code=404, detail="No data available in the database")

        for doc in documents:
            doc["_id"] = str(doc["_id"])

        return {"message": "All weather data retrieved successfully", "data": documents}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/get_data/{date}")
async def get_weather_data_by_date(date: str):
    try:
        document = collection.find_one({"date": date})

        if not document:
            raise HTTPException(status_code=404, detail=f"No data found for date: {date}")

        return {
            "date": document["date"],
            "records": document["records"]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))