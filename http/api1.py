import requests

url = "https://earthquake.usgs.gov/fdsnws/event/1/query?"

response = requests.get(url,
                        headers={'Accept': 'application/json'},
                        params={"format": "geojson",
                                "starttime": input("Enter the start time (yyyy-mm-dd): "),
                                "endtime": input("Enter the end time (yyyy-mm-dd): "),
                                "latitude": input("Enter the latitude: "),
                                "longitude": input("Enter the longitude: "),
                                "maxradiuskm": input("Enter the maximum radius in km: "),
                                "minmagnitude": input("Enter the minimum magnitude: "),
                                })

data = response.json()

# print(data["features"][0]["properties"]["place"])

for i, e in enumerate(data["features"], 1):
    print(f'{i}. Place: {e["properties"]["place"]}. Magnitude: {e["properties"]["mag"]}.')
