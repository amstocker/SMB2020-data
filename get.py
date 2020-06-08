import json
from pprint import pprint

import requests


with open("login.json") as f:
    login_info = json.loads(f.read())

with open("tournaments.json") as f:
    tournament_ids = json.loads(f.read())

API_URL = "https://{username}:{api-key}@api.challonge.com/v1/".format(**login_info)


def get_tournament(tournament_id):
    path = "tournaments/{id}/matches.json"
    url = API_URL + path.format(id=tournament_id)
    r = requests.get(url)
    return r.json()


for tournament_id in tournament_ids:
    tournament_data = get_tournament(tournament_id)
    with open("data/{id}.json".format(id=tournament_id), "w") as f:
        json.dump(tournament_data, f)