import json
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

def load_tournament(tournament_id):
    filename = "data/{id}.json"
    with open(filename.format(id=tournament_id)) as f:
        return json.loads(f.read())

def load_tournament_participants(tournament_id):
    filename = "data/{id}_participants.json"
    with open(filename.format(id=tournament_id)) as f:
        return json.loads(f.read())

def load_tournaments():
    return [{
        "id": t_id,
        "index": tournament_ids.index(t_id) + 1,
        "matches": load_tournament(t_id),
        "participants": load_tournament_participants(t_id)
     } for t_id in tournament_ids]

def build_id_to_name_map():
    with open("namemap.json") as f:
        name_map = json.loads(f.read())

    # Build reverse lookup for names
    reverse_name_map = {}
    for k, v in name_map.items():
        for name in v:
            reverse_name_map[name] = k
    
    id_to_name = {}
    tournaments = load_tournaments()
    for t in tournaments:
        participants = t["participants"]
        for p in participants:
            p_id = p["participant"]["id"]
            p_name = p["participant"]["display_name"]
            id_to_name[p_id] = reverse_name_map[p_name]
    
    with open("data/id_to_name.json", "w") as f:
        json.dump(id_to_name, f, indent=4, sort_keys=True)

def load_id_to_name_map():
    with open("data/id_to_name.json") as f:
        return json.loads(f.read())

if __name__ == "__main__":
    dump_tournaments()
    dump_tournament_participants()
    build_id_to_name_map()