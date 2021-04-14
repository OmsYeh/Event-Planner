import requests
from urllib.parse import urlparse, parse_qsl, urlencode

GOOGLE_API = "AIzaSyAiqyA_m_vpAGigBzRYSnER2gCq-ftl54Q"


class GoogleMapsClient(object):
    lat = None
    lng = None
    data_type = 'json'
    location_query = None
    api_key = None

    def __init__(self, api_key=None, address_or_postal_code=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if api_key is None:
            raise Exception("API key is required")
        self.api_key = api_key
        self.location_query = address_or_postal_code
        if self.location_query is not None:
            self.extract_lat_lng()

    def extract_lat_lng(self):
        endpoint = f"https://maps.googleapis.com/maps/api/geocode/{self.data_type}"
        params = {"address": self.location_query, "key": self.api_key}
        url_params = urlencode(params)
        url = f"{endpoint}?{url_params}"
        r = requests.get(url)
        if r.status_code not in range(200, 299):
            return {}
        latlng = {}
        try:
            latlng = r.json()['results'][0]['geometry']['location']
        except:
            pass
        lat, lng = latlng.get("lat"), latlng.get("lng")
        self.lat = lat
        self.lng = lng
        return lat, lng


client = GoogleMapsClient(api_key=GOOGLE_API, address_or_postal_code="1600 Amphitheatre Parkway , Mountain View, CA")
print(client.lat, client.lng)

# data_type = "json"
# endpoint = f"https://maps.googleapis.com/maps/api/geocode/{data_type}"
# params = {"address": "1600 Amphitheatre Parkway , Mountain View, CA", "key": GOOGLE_API_KEY}
# url_params = urlencode( params )
#
# url = f"{endpoint}?{url_params}"
# print( url )
#
#
# def extract_lat_lng(address_or_postalcode, data_type='json'):
#     endpoint = f"https://maps.googleapis.com/maps/api/geocode/{data_type}"
#     params = {"address": address_or_postalcode, "key": GOOGLE_API}
#     url_params = urlencode( params )
#     url = f"{endpoint}?{url_params}"
#     r = requests.get( url )
#     if r.status_code not in range( 200, 299 ):
#         return {}
#     latlng = {}
#     try:
#         latlng = r.json()['results'][0]['geometry']['location']
#     except:
#         pass
#     return latlng.get( "lat" ), latlng.get( "lng" )
#
#
# extract_lat_lng( "28 Khayim Weizman , Givat Shmuel, Israel" )
#
# to_parse = "https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway+%2C+Mountain+View%2C+CA&key=AIzaSyB3A8LoJnqaWFvWpki7keVL0r4MOK5mWPc"
# urlparse( to_parse )
# parsed_url = urlparse( to_parse )
# query_string = parsed_url.query
# print( query_string )
#
# query_tuple = parse_qsl( query_string )
# print( query_tuple )
#
# query_dict = dict( query_tuple )
# print( query_dict )
#
# endpoint = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}"
# print( endpoint )
#
# lat, lng = 32.0765839, 34.8478908
# base_endpoint_places = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json"
# params = {
#     "key": GOOGLE_API_KEY,
#     "input": "sushi",
#     "inputtype": "textquery",
#     "fields": "formatted_address,name,geometry,permanently_closed,place_id"
# }
# locationbias = f"point:{lat},{lng}"
# use_circular = False
# if use_circular:
#     radius = 10000
#     locationbias = f"circle:{radius}@{lat},{lng}"
#
# params['locationbias'] = locationbias
#
# params_encoded = urlencode( params )
# places_endpoint = f"{base_endpoint_places}?{params_encoded}"
# print( places_endpoint )
#
# r = requests.get( places_endpoint )
# print( r.status_code )
# r.json()
#
# places_endpoint_2 = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
# params_2 = {
#     "key": GOOGLE_API_KEY,
#     "location": f"{lat},{lng}",
#     "radius": 1500,
#     "keyword": "sushi"
# }
# params_2_encoded = urlencode( params_2 )
# places_url = f"{places_endpoint_2}?{params_2_encoded}"
# r2 = requests.get( places_url )
# r2.json()
#
# # detail lookup
#
# place_id = "ChIJUd28fgtLHRURxRh9DdfXcQk"
# detail_base_endpoint = "https://maps.googleapis.com/maps/api/place/details/json"
# detail_params = {
#     "place_id": f"{place_id}",
#     "fields": "formatted_address,name,rating,formatted_phone_number",
#     "key": GOOGLE_API_KEY
# }
#
# detail_params_encoded = urlencode( detail_params )
#
# detail_url = f"{detail_base_endpoint}?{detail_params_encoded}"
# r = requests.get( detail_url )
# r.json()
