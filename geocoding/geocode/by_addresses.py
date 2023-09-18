import requests

class Get_by_addresses:

        def __init__(self):
            self.url = "https://nominatim.openstreetmap.org/search"

        def get_coord(self,city,street):
            params = {   "city":city,
                        "street" :street,
                        "format" :'json'
            }
            res = requests.get(url=self.url,params=params)
            if res.ok:
                latitude = res.json()[0]['lat']
                longitude = res.json()[0]['lon']
                return latitude,longitude

        def get_osm_id_by_country(self,country):
            params = {
                'country' :country,
                "format": 'json'
            }
            res = requests.get(url=self.url, params=params)
            if res.ok:
                return res.json()[0]['osm_id']

        def get_objects_volume_in_city(self,city,street):
            params = {
                'city':city,
                "street": street,
                'format':"json"
            }
            res = requests.get(url=self.url,params=params)
            if res.ok:
                return len(res.json())

        def test_squash(self):
            return "Squash"