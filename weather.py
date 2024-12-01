import requests
from dotenv import load_dotenv
import os
from datetime import datetime
import re

load_dotenv()

def fetch_weather_data():
    # return [{'Date': '2024-11-30', 'Hour': 17, 'Minute': 30, 'Air Temp': 20, 'Cloud Opacity': 49, 'GHI': 0},
    #     {'Date': '2024-11-30', 'Hour': 18, 'Minute': 0, 'Air Temp': 20, 'Cloud Opacity': 53, 'GHI': 0},
    #     {'Date': '2024-11-30', 'Hour': 18, 'Minute': 30, 'Air Temp': 20, 'Cloud Opacity': 56, 'GHI': 0},
    #     {'Date': '2024-11-30', 'Hour': 19, 'Minute': 0, 'Air Temp': 20, 'Cloud Opacity': 59, 'GHI': 0},
    #     {'Date': '2024-11-30', 'Hour': 19, 'Minute': 30, 'Air Temp': 20, 'Cloud Opacity': 61, 'GHI': 0},
    #     {'Date': '2024-11-30', 'Hour': 20, 'Minute': 0, 'Air Temp': 20, 'Cloud Opacity': 66, 'GHI': 0},
    #     {'Date': '2024-11-30', 'Hour': 20, 'Minute': 30, 'Air Temp': 20, 'Cloud Opacity': 62, 'GHI': 0},
    #     {'Date': '2024-11-30', 'Hour': 21, 'Minute': 0, 'Air Temp': 20, 'Cloud Opacity': 54, 'GHI': 0},
    #     {'Date': '2024-11-30', 'Hour': 21, 'Minute': 30, 'Air Temp': 20, 'Cloud Opacity': 53, 'GHI': 0},
    #     {'Date': '2024-11-30', 'Hour': 22, 'Minute': 0, 'Air Temp': 20, 'Cloud Opacity': 53, 'GHI': 0},
    #     {'Date': '2024-11-30', 'Hour': 22, 'Minute': 30, 'Air Temp': 20, 'Cloud Opacity': 53, 'GHI': 0},
    #     {'Date': '2024-11-30', 'Hour': 23, 'Minute': 0, 'Air Temp': 19, 'Cloud Opacity': 53, 'GHI': 0},
    #     {'Date': '2024-11-30', 'Hour': 23, 'Minute': 30, 'Air Temp': 19, 'Cloud Opacity': 53, 'GHI': 0},
    #     {'Date': '2024-12-01', 'Hour': 0, 'Minute': 0, 'Air Temp': 19, 'Cloud Opacity': 53, 'GHI': 0},
    #     {'Date': '2024-12-01', 'Hour': 0, 'Minute': 30, 'Air Temp': 19, 'Cloud Opacity': 52, 'GHI': 0},
    #     {'Date': '2024-12-01', 'Hour': 1, 'Minute': 0, 'Air Temp': 19, 'Cloud Opacity': 52, 'GHI': 0},
    #     {'Date': '2024-12-01', 'Hour': 1, 'Minute': 30, 'Air Temp': 19, 'Cloud Opacity': 51, 'GHI': 12},
    #     {'Date': '2024-12-01', 'Hour': 2, 'Minute': 0, 'Air Temp': 19, 'Cloud Opacity': 50, 'GHI': 47},
    #     {'Date': '2024-12-01', 'Hour': 2, 'Minute': 30, 'Air Temp': 20, 'Cloud Opacity': 51, 'GHI': 91},
    #     {'Date': '2024-12-01', 'Hour': 3, 'Minute': 0, 'Air Temp': 21, 'Cloud Opacity': 55, 'GHI': 127},
    #     {'Date': '2024-12-01', 'Hour': 3, 'Minute': 30, 'Air Temp': 22, 'Cloud Opacity': 55, 'GHI': 170},
    #     {'Date': '2024-12-01', 'Hour': 4, 'Minute': 0, 'Air Temp': 22, 'Cloud Opacity': 51, 'GHI': 229},
    #     {'Date': '2024-12-01', 'Hour': 4, 'Minute': 30, 'Air Temp': 23, 'Cloud Opacity': 48, 'GHI': 282},
    #     {'Date': '2024-12-01', 'Hour': 5, 'Minute': 0, 'Air Temp': 24, 'Cloud Opacity': 46, 'GHI': 324},
    #     {'Date': '2024-12-01', 'Hour': 5, 'Minute': 30, 'Air Temp': 25, 'Cloud Opacity': 44, 'GHI': 359},
    #     {'Date': '2024-12-01', 'Hour': 6, 'Minute': 0, 'Air Temp': 26, 'Cloud Opacity': 43, 'GHI': 386},
    #     {'Date': '2024-12-01', 'Hour': 6, 'Minute': 30, 'Air Temp': 26, 'Cloud Opacity': 40, 'GHI': 405},
    #     {'Date': '2024-12-01', 'Hour': 7, 'Minute': 0, 'Air Temp': 27, 'Cloud Opacity': 38, 'GHI': 416},
    #     {'Date': '2024-12-01', 'Hour': 7, 'Minute': 30, 'Air Temp': 27, 'Cloud Opacity': 38, 'GHI': 405},
    #     {'Date': '2024-12-01', 'Hour': 8, 'Minute': 0, 'Air Temp': 27, 'Cloud Opacity': 39, 'GHI': 372},
    #     {'Date': '2024-12-01', 'Hour': 8, 'Minute': 30, 'Air Temp': 27, 'Cloud Opacity': 41, 'GHI': 327},
    #     {'Date': '2024-12-01', 'Hour': 9, 'Minute': 0, 'Air Temp': 27, 'Cloud Opacity': 43, 'GHI': 273},
    #     {'Date': '2024-12-01', 'Hour': 9, 'Minute': 30, 'Air Temp': 27, 'Cloud Opacity': 45, 'GHI': 219},
    #     {'Date': '2024-12-01', 'Hour': 10, 'Minute': 0, 'Air Temp': 27, 'Cloud Opacity': 46, 'GHI': 166},
    #     {'Date': '2024-12-01', 'Hour': 10, 'Minute': 30, 'Air Temp': 26, 'Cloud Opacity': 46, 'GHI': 114},
    #     {'Date': '2024-12-01', 'Hour': 11, 'Minute': 0, 'Air Temp': 26, 'Cloud Opacity': 48, 'GHI': 66},
    #     {'Date': '2024-12-01', 'Hour': 11, 'Minute': 30, 'Air Temp': 25, 'Cloud Opacity': 48, 'GHI': 27},
    #     {'Date': '2024-12-01', 'Hour': 12, 'Minute': 0, 'Air Temp': 25, 'Cloud Opacity': 45, 'GHI': 3},
    #     {'Date': '2024-12-01', 'Hour': 12, 'Minute': 30, 'Air Temp': 24, 'Cloud Opacity': 43, 'GHI': 0},
    #     {'Date': '2024-12-01', 'Hour': 13, 'Minute': 0, 'Air Temp': 24, 'Cloud Opacity': 44, 'GHI': 0},
    #     {'Date': '2024-12-01', 'Hour': 13, 'Minute': 30, 'Air Temp': 24, 'Cloud Opacity': 44, 'GHI': 0},
    #     {'Date': '2024-12-01', 'Hour': 14, 'Minute': 0, 'Air Temp': 24, 'Cloud Opacity': 43, 'GHI': 0},
    #     {'Date': '2024-12-01', 'Hour': 14, 'Minute': 30, 'Air Temp': 24, 'Cloud Opacity': 43, 'GHI': 0},
    #     {'Date': '2024-12-01', 'Hour': 15, 'Minute': 0, 'Air Temp': 24, 'Cloud Opacity': 43, 'GHI': 0},
    #     {'Date': '2024-12-01', 'Hour': 15, 'Minute': 30, 'Air Temp': 24, 'Cloud Opacity': 43, 'GHI': 0},
    #     {'Date': '2024-12-01', 'Hour': 16, 'Minute': 0, 'Air Temp': 24, 'Cloud Opacity': 42, 'GHI': 0},
    #     {'Date': '2024-12-01', 'Hour': 16, 'Minute': 30, 'Air Temp': 23, 'Cloud Opacity': 41, 'GHI': 0},
    #     {'Date': '2024-12-01', 'Hour': 17, 'Minute': 0, 'Air Temp': 23, 'Cloud Opacity': 40, 'GHI': 0},
    #     {'Date': '2024-12-01', 'Hour': 17, 'Minute': 30, 'Air Temp': 23, 'Cloud Opacity': 39, 'GHI': 0},
    #     {'Date': '2024-12-01', 'Hour': 18, 'Minute': 0, 'Air Temp': 23, 'Cloud Opacity': 38, 'GHI': 0},
    #     {'Date': '2024-12-01', 'Hour': 18, 'Minute': 30, 'Air Temp': 22, 'Cloud Opacity': 40, 'GHI': 0},
    #     {'Date': '2024-12-01', 'Hour': 19, 'Minute': 0, 'Air Temp': 22, 'Cloud Opacity': 46, 'GHI': 0},
    #     {'Date': '2024-12-01', 'Hour': 19, 'Minute': 30, 'Air Temp': 22, 'Cloud Opacity': 48, 'GHI': 0},
    #     {'Date': '2024-12-01', 'Hour': 20, 'Minute': 0, 'Air Temp': 22, 'Cloud Opacity': 46, 'GHI': 0},
    #     {'Date': '2024-12-01', 'Hour': 20, 'Minute': 30, 'Air Temp': 21, 'Cloud Opacity': 44, 'GHI': 0},
    #     {'Date': '2024-12-01', 'Hour': 21, 'Minute': 0, 'Air Temp': 21, 'Cloud Opacity': 42, 'GHI': 0},
    #     {'Date': '2024-12-01', 'Hour': 21, 'Minute': 30, 'Air Temp': 21, 'Cloud Opacity': 41, 'GHI': 0},
    #     {'Date': '2024-12-01', 'Hour': 22, 'Minute': 0, 'Air Temp': 20, 'Cloud Opacity': 42, 'GHI': 0},
    #     {'Date': '2024-12-01', 'Hour': 22, 'Minute': 30, 'Air Temp': 20, 'Cloud Opacity': 42, 'GHI': 0},
    #     {'Date': '2024-12-01', 'Hour': 23, 'Minute': 0, 'Air Temp': 20, 'Cloud Opacity': 43, 'GHI': 0},
    #     {'Date': '2024-12-01', 'Hour': 23, 'Minute': 30, 'Air Temp': 20, 'Cloud Opacity': 44, 'GHI': 0}]

    url = "https://api.solcast.com.au/weather_sites/ee60-9d0b-7ce3-1710/forecasts?format=json"
    token = os.getenv("API_TOKEN")
    headers = {"Authorization": f"Bearer {token}"}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            
            forecasts = data.get("forecasts", [])
            if forecasts:
                forecast_list = []
                for forecast in forecasts:
                    air_temp = int(forecast.get("air_temp"))
                    cloud_opacity = int(forecast.get("cloud_opacity"))
                    ghi = int(forecast.get("ghi"))

                    period_end = forecast.get("period_end")
                    period_end = re.sub(r'(\.\d{6})\d+', r'\1', period_end)
                    dt = datetime.strptime(period_end, "%Y-%m-%dT%H:%M:%S.%fZ")
                    date = dt.date().strftime("%Y-%m-%d")
                    hour = dt.hour
                    minute = dt.minute
                    
                    forecast_list.append({
                        "Date": date,
                        "Hour": hour,
                        "Minute": minute, 
                        "Air Temp": air_temp,
                        "Cloud Opacity": cloud_opacity,
                        "GHI": ghi
                    })
                print('Success')
                return forecast_list
            else:
                raise Exception("No forecast data available.")
        else:
            raise Exception(f"Failed to fetch data. Status code: {response.status_code}") 

    except Exception as e:
        return f"An error occurred: {e}"
    

# # Example usage
# forecast_data = fetch_weather_data()

# # Print the fetched data
# if isinstance(forecast_data, list):
#     for forecast in forecast_data:
#         print(forecast)
# else:
#     print(forecast_data)
