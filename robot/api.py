import requests
search_url = "https://nominatim.openstreetmap.org/search"

def get_limit(limit=None):
    # if not limit:
    #     params_list = {
    #         "amenity": "pub",
    #         "format": "json"
    #     }
    # else:
    params_list = {
            "amenity":"pub",
            "limit": limit,
            "format":"json"
            }
    resp = requests.get(search_url,params=params_list)
    if resp.ok:
        return resp.json()

print(get_limit())