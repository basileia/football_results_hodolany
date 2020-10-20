import json


def load_json():
    with open('tables.json') as json_file:
        data = json.load(json_file)
    return data


second_teams = []
wanted_team = "FC Sigma Hodolany (2)"
results = load_json()
print(results[2])
