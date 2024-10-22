import requests

# these are the coords of ucf
LAT = 28.6044
LON = -81.1994

# api url
url = "https://api.weather.gov/"

# gets the current forecast from the grid the coords are located in
def getForcast(latitude, longitude):
    response = requests.get(f"{url}points/{latitude},{longitude}")
    data = response.json()

    forecastResponse = requests.get(data['properties']['forecast'])
    forecast = forecastResponse.json()

    return forecast

# prints time name and wind speed of grid the coords are located in
def printWindInfo(latitude, longitude):
    forecast = getForcast(latitude, longitude)
    periodName = forecast['properties']['periods'][0]['name']
    windSpeed = forecast['properties']['periods'][0]['windSpeed']

    print(f'{periodName}\nWind Speed: {windSpeed}')

# run
def main():
    printWindInfo(LAT, LON)
    
main()