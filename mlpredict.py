import joblib
from datetime import datetime
import pandas as pd

from weather import fetch_weather_data


def calculate_cell_temp(air_temp, irrad):
    return air_temp + ((45 - 20) / 8) * (irrad / 500)

def apply_cloud_opacity_noise(cloud_opacity, gti_original, max_noise_factor=0.3):
    noise_factor = (cloud_opacity / 100) * max_noise_factor
    gti_noisy = gti_original * (1 - noise_factor)
    return int(gti_noisy)


def ml_model_predict(api_data):
    forecast_data = []
    model = joblib.load('./trained_ML_model/model.pkl')
    scaler = joblib.load('./trained_ML_model/scaler.pkl')

    for data in api_data:
        date = data['Date']
        hours = data['Hour']
        minutes = data['Minute']
        air_temp = int(data['Air Temp'])  
        irrad = int(data['GHI'])  
        cloud_opacity = int(data['Cloud Opacity'])

        irrad = apply_cloud_opacity_noise(cloud_opacity, irrad)
        cell_temperature = calculate_cell_temp(air_temp, irrad)

        feature_names = ['irrad', 'cell_temperature', 'hours', 'minutes']
        features = [[irrad, cell_temperature, hours, minutes]]
        features_df = pd.DataFrame(features, columns=feature_names)
        scaled_features = scaler.transform(features_df)

        predicted_power = model.predict(scaled_features)
        predicted_power = 0.0 if predicted_power[0] < 0 else predicted_power[0]

        forecast_data.append({
            'date' : date,
            'hours': hours,
            'minutes': minutes,
            'irrad': irrad,
            'cell_temperature': cell_temperature,
            'predicted_power': predicted_power
        })
    print('Success')
    return forecast_data


# api_data = fetch_weather_data()
# print("*****************************************")
# print(api_data)
# ml_model_predict(api_data=api_data)
