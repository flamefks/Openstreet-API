import requests
def get_coord_by_street(lat,lon):
    url = "https://nominatim.openstreetmap.org/reverse"
    params = {"lat": lat,
              "lon": lon,
              "format": 'json',
              }
    res = requests.get(url=url, params=params)
    return res.json()

def get_street_by_coord(street,city = None,country=None):
    url = "https://nominatim.openstreetmap.org/search"
    params = {      "city":city,
                    "street" :street,
                    "country" :country,
                    "format" :'json'
    }
    res = requests.get(url=url,params=params)
    if res.ok:
        latitude = res.json()[0]['lat']
        longitude = res.json()[0]['lon']
        return latitude,longitude
print(get_street_by_coord("15 Первомайская",city="Екатеринбург"))
print(get_coord_by_street("44.50155","11.33989"))
