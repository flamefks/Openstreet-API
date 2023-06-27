import requests

class Get_by_coord:

    def __init__(self):
        self.url = "https://nominatim.openstreetmap.org/reverse"

    def get_address(self,lat, lon):
        params = {"lat": lat,
                  "lon": lon,
                  "format": 'json',
                  }
        res = requests.get(url=self.url, params=params)
        if res.ok:
            # return res.json()['display_name']
            return res.json()

    def get_excat_coord(self,lat,lon):
        params = {"lat": lat,
                  "lon": lon,
                  "format": 'json',
                  }
        res = requests.get(url=self.url, params=params)
        if res.ok:
            return res.json()['lat'], res.json()['lon']

