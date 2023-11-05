import requests
import urllib.request
import params
import json


def from_api_as_json(save_to_file=False):
    api_url = params.api_link

    with urllib.request.urlopen(api_url) as url:
        obstructions = json.load(url)
    if save_to_file:
        with open('./data/obstructions.json', 'w') as outfile:
            json.dump(obstructions, outfile)
    return obstructions
