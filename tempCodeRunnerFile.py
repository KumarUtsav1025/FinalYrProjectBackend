# Example usage
forecast_data = fetch_forecast_data()

# Print the fetched data
if isinstance(forecast_data, list):
    for forecast in forecast_data:
        print(forecast)
else:
    print(forecast_data)
