import json


def load_json(file_name):
    """
    Loads given json file
    """
    with open(file_name, encoding="utf-8") as json_file:
        data = json.load(json_file)
    return data


def get_info():
    """
    Get information about football matches, returns list with:
    date, home team, away team and score
    """
    wanted_team = "FC Sigma Hodolany (2)"
    matches_info = []

    results = load_json("tables.json")

    for j in range(1, len(results)):

        for num, i in zip(results[j]["hosté"], results[j]["domácí"]):
            if wanted_team in results[j]["hosté"][num]:
                matches_info.append([results[j]["datum a čas"][num],
                                    results[j]["domácí"][num],
                                    wanted_team, results[j]["skóre"][num]])

            if wanted_team in results[j]["domácí"][i]:
                matches_info.append([results[j]["datum a čas"][i],
                                    wanted_team, results[j]["hosté"][i],
                                    results[j]["skóre"][i]])
    return remove_pk_zero(matches_info)


def remove_pk_zero(matches_info):
    """
    Removes zero penalty kicks from results
    """
    for i in range(len(matches_info)):
        matches_info[i][3] = matches_info[i][3].replace(" (PK:0:0)", "")
        print(matches_info[i][3])
    return matches_info


print(get_info())
