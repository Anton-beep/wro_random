import requests

API_TEMPLATE = 'https://www.random.org/'


def get_random_range(min, max):
    return list(map(int, requests.get(
        API_TEMPLATE + f'sequences/?min={min}&max={max}&col=1&format=plain&rnd=new').text.split(
        '\n')[:-1]))
