import requests
import math


def check_response(response):
    if not response:
        print("Ошибка выполнения запроса:")
        print(response.url)
        print("Http статус:", response.status_code, "(", response.reason, ")")


def check_coordinates(coord: float, delta: float, direction: str):
    if direction == 'x':
        if coord + delta > 180 or coord + delta < -180:
            return coord
    elif direction == 'y':
        if coord + delta > 90 or coord + delta < -90:
            return coord
    return coord + delta


def get_coords(place: str):
    geocode_url = "https://geocode-maps.yandex.ru/1.x/"
    params = {"apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
              "geocode": f"{place}",
              "format": "json"}
    response = requests.get(geocode_url, params)
    if response:
        r = response.json()
        if int(r["response"]["GeoObjectCollection"]['metaDataProperty']['GeocoderResponseMetaData']['found']) > 0:
            ll = r["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
            return ll.replace(" ", ",")
    return None


def get_spn(coords: str):
    geocode_url = "https://geocode-maps.yandex.ru/1.x/"
    params = {"apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
              "geocode": coords.replace(" ", ","),
              "format": "json"}
    response = requests.get(geocode_url, params)
    if response:
        r = response.json()
        envelop = r["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]['boundedBy']['Envelope']
        lcorner = envelop['lowerCorner'].split()
        ucorner = envelop['upperCorner'].split()
        x = float(ucorner[0]) - float(lcorner[0])
        y = float(ucorner[1]) - float(lcorner[1])
        return ",".join(map(str, [x, y]))
    return None


def get_image(coords: str, zoom=None, layers='map', points=None):
    if points is None:
        points = []
    static_map_url = 'http://static-maps.yandex.ru/1.x/'
    params = {'ll': coords.replace(' ', ','),
              'pt': '~'.join(points),
              'l': layers,
              'size': '650,450'}
    if zoom is None:
        params['spn'] = get_spn(coords)
    else:
        params['z'] = zoom
    response = requests.get(static_map_url, params)
    if response:
        return response.content
    return None


def get_description(place: str):
    description = f"{get_coords(place)}"
    return description


def get_points(*places):
    return map(get_description, places)


def get_address(coords: str, postcode: bool):
    geocode_url = "https://geocode-maps.yandex.ru/1.x/"
    params = {"apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
              "geocode": coords.replace(" ", ","),
              "format": "json"}
    response = requests.get(geocode_url, params)
    if response:
        r = response.json()
        r = r["response"]["GeoObjectCollection"]["featureMember"][0][
            "GeoObject"]["metaDataProperty"]["GeocoderMetaData"]
        if postcode and 'postal_code' in r['Address']:
            address = f"{r['text']}, {r['Address']['postal_code']}"
        elif postcode:
            address = r['text'] + ', нет индекса'
        else:
            address = r['text']
        return address
    return None


def get_organization(coords: str):
    address = "https://search-maps.yandex.ru/v1/"
    coords123 = list(map(float, coords.split(',')))
    params = {"apikey": "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3",
              "text": "Организация",
              "lang": "ru_RU",
              "type": "biz",
              "ll": f"{coords123[0]},{coords123[1]}",
              "spn": "0.003,0.003",
              "results": "1",
              "rspn": "1",
              "format": "json"}
    request = requests.get(address, params)
    request = request.json()
    print(request)
    if len(request["features"]) != 0:
        coordss = request["features"][-1]["geometry"]["coordinates"]
        return f'{coordss[0]},{coordss[1]}'
    return None


def lonlat_distance(a, b):
    degree_to_meters_factor = 111 * 1000
    a_lon, a_lat = a
    b_lon, b_lat = b
    radians_lattitude = math.radians((a_lat + b_lat) / 2.)
    lat_lon_factor = math.cos(radians_lattitude)
    dx = abs(a_lon - b_lon) * degree_to_meters_factor * lat_lon_factor
    dy = abs(a_lat - b_lat) * degree_to_meters_factor
    distance = math.sqrt(dx * dx + dy * dy)
    return distance
