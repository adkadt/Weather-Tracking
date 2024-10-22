import requests
import json

LAT = 28.6044
LON = -81.1994

url = "https://api.weather.gov/"

def getGridData():
    response = requests.get(f"{url}points/{LAT},{LON}")
    data = response.json()

    gridURL = data['properties']['forecastGridData']
    print(gridURL)

    # return gridX, gridY

# def getDataAtLatLon():
#     getGridPoint()




def main():
    print(f"{url}points/{LAT},{LON}")
    getGridData()
    print()

main()