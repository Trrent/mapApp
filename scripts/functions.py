import requests


def check_response(response):
    if not response:
        print("Ошибка выполнения запроса:")
        print(response.url)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        exit()


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
    check_response(response)
    r = response.json()
    ll = r["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["Point"]["pos"]
    return ll.replace(" ", ",")


def get_spn(coords: str):
    geocode_url = "https://geocode-maps.yandex.ru/1.x/"
    params = {"apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
              "geocode": coords.replace(" ", ","),
              "format": "json"}
    response = requests.get(geocode_url, params)
    check_response(response)
    r = response.json()
    envelop = r["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]['boundedBy']['Envelope']
    lcorner = envelop['lowerCorner'].split()
    ucorner = envelop['upperCorner'].split()
    x = float(ucorner[0]) - float(lcorner[0])
    y = float(ucorner[1]) - float(lcorner[1])
    return ",".join(map(str, [x, y]))


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
    check_response(response)
    return response.content


def get_description(place: str):
    description = f"{get_coords(place)}"
    return description


def get_points(*places):
    return map(get_description, places)


def get_address(coords: str):
    geocode_url = "https://geocode-maps.yandex.ru/1.x/"
    params = {"apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
              "geocode": coords.replace(" ", ","),
              "format": "json"}
    response = requests.get(geocode_url, params)
    check_response(response)
    r = response.json()
    address = \
        r["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["metaDataProperty"]["GeocoderMetaData"][
            "text"]
    return address
