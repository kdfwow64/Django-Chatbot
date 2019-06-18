import json, requests, re

def get_country_name(ip_address):
    try:
        url = "http://api.ipstack.com/{ip_address}?access_key=e6f85c3f9fa9615ea504b4f4ab285387".format(
            ip_address=ip_address
        )
        # url = "http://ip-api.com/json/{}".format(ip_address)
        r = requests.get(url)
        data = r.json()
        d = data["country_name"]
        return d
    except KeyError:
        return "Country not found"
