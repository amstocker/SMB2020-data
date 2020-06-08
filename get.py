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

def dump_tournaments():
    for tournament_id in tournament_ids:
        filename = "data/{id}.json".format(id=tournament_id)
        with open(filename, "w") as f:
            tournament_data = get_tournament(tournament_id)
            json.dump(tournament_data, f, indent=4, sort_keys=True)


def get_tournament_participants(tournament_id):
    path = "tournaments/{id}/participants.json"
    url = API_URL + path.format(id=tournament_id)
    r = requests.get(url)
    return r.json()

def dump_tournament_participants():
    for tournament_id in tournament_ids:
        filename = "data/{id}_participants.json".format(id=tournament_id)
        with open(filename, "w") as f:
            participants_data = get_tournament_participants(tournament_id)
            json.dump(participants_data, f, indent=4, sort_keys=True)