import json
import datetime


def load_json(file_name):
    """
    Loads given json file
    """
    with open(file_name, encoding="utf-8") as json_file:
        data = json.load(json_file)
    return data


def get_info(number):
    """
    Get information about a football match by table number, returns list with:
    date, home team, away team and score
    Date is reformatting
    """
    wanted_team = "FC Sigma Hodolany (2)"
    results = load_json("table" + str(number) + ".json")

    for num, i in zip(results["hosté"], results["domácí"]):
        if wanted_team in results["hosté"][num]:
            info = [results["datum a čas"][num], results["domácí"][num],
                    wanted_team, results["skóre"][num]]

        if wanted_team in results["domácí"][i]:
            info = [results["datum a čas"][i], wanted_team,
                    results["hosté"][i], results["skóre"][i]]
    info[0] = time_formatting(info[0])
    return info


def time_formatting(date_time):
    """
    Returns reformatting date and time
    """
    return datetime.datetime.strptime(date_time, '%d.%m.%Y %H:%M')


def sort_by_date(list_info):
    return sorted(list_info, key=lambda x: x[0])


def get_matches_info():
    """
    Get info about football matches in the competition
    Returns lists of matches sorted by date
    """
    matches_info = []
    for i in range(1, 30):
        matches_info.append(get_info(i))
    sorted_matches_info_date = sort_by_date(matches_info)
    return sorted_matches_info_date


print(get_matches_info())
