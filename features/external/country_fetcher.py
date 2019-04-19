import json, requests, re

def get_country_name(ip_address):
    try:
        url = "http://ip-api.com/json/{}".format(ip_address)
        r = requests.get(url)
        data = r.json()
        d = data["country"]
        return d
    except KeyError:
        return "Country not found"
